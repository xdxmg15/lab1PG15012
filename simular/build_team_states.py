import pandas as pd
import numpy as np
import os

from simular.world_cup_loader import (
    load_world_cup_schedule,
    get_all_teams
)
from simular.team_utils import (
    normalize_team_name
)


def calculate_elo_ratings(

    matches,
    k=20,
    initial_rating=1500
):

    ratings = {}

    for _, row in matches.iterrows():

        home = normalize_team_name(
            row['home_team']
        )

        away = normalize_team_name(
            row['away_team']
        )

        home_elo = ratings.get(
            home,
            initial_rating
        )

        away_elo = ratings.get(
            away,
            initial_rating
        )

        expected_home = 1 / (
            1 + 10 ** (
                (away_elo - home_elo) / 400
            )
        )

        # ACTUAL RESULT

        if row['home_score'] > row['away_score']:

            actual_home = 1

        elif row['home_score'] < row['away_score']:

            actual_home = 0

        else:

            actual_home = 0.5

        new_home = (
            home_elo
            +
            k * (
                actual_home
                -
                expected_home
            )
        )

        new_away = (
            away_elo
            +
            k * (
                (1 - actual_home)
                -
                (1 - expected_home)
            )
        )

        ratings[home] = new_home
        ratings[away] = new_away

    return ratings


def build_team_states():

    script_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    csv_path = os.path.join(
        script_dir,
        '..',
        'csv',
        'results.csv'
    )

    results = pd.read_csv(
        csv_path,
        parse_dates=['date']
    )

    results = results.sort_values(
        'date'
    )

    # CALCULATE ELO

    elo_ratings = calculate_elo_ratings(
        results
    )

    team_states = {}

    schedule = load_world_cup_schedule()

    teams = get_all_teams(
        schedule
    )

    for team in teams:

        # LAST MATCHES HOME

        home_matches = results[
            results['home_team'] == team
        ]

        # LAST MATCHES AWAY

        away_matches = results[
            results['away_team'] == team
        ]

        all_matches = pd.concat([

            home_matches,
            away_matches

        ]).sort_values(
            'date'
        ).tail(5)

        if len(all_matches) == 0:

            continue

        wins = 0
        goals_for = []
        goals_against = []

        for _, row in all_matches.iterrows():

            if row['home_team'] == team:

                gf = row['home_score']
                ga = row['away_score']

            else:

                gf = row['away_score']
                ga = row['home_score']

            goals_for.append(gf)
            goals_against.append(ga)

            if gf > ga:

                wins += 1

        winrate = wins / len(all_matches)

        avg_gf = np.mean(goals_for)

        avg_ga = np.mean(goals_against)

        goal_diff = avg_gf - avg_ga

        team_states[team] = {

            'elo': elo_ratings.get(
                team,
                1500
            ),

            'winrate_last_5':
                winrate,

            'goals_for_last_5':
                avg_gf,

            'goals_against_last_5':
                avg_ga,

            'goal_diff_last_5':
                goal_diff
        }

    return team_states