import pandas as pd

from simular.team_utils import (
    normalize_team_name
)

DEFAULT_TEAM_STATE = {

    'elo': 1500,

    'winrate_last_5': 0.5,

    'goals_for_last_5': 1.2,

    'goals_against_last_5': 1.2,

    'goal_diff_last_5': 0
}


def build_match_features(

    home_team,
    away_team,

    team_states,

    neutral=1
):

    # NORMALIZE TEAM NAMES

    home_team = normalize_team_name(
        home_team
    )

    away_team = normalize_team_name(
        away_team
    )

    # FALLBACK STATES

    if home_team not in team_states:

        print(
            f'WARNING: {home_team} not found'
        )

        team_states[
            home_team
        ] = DEFAULT_TEAM_STATE.copy()

    if away_team not in team_states:

        print(
            f'WARNING: {away_team} not found'
        )

        team_states[
            away_team
        ] = DEFAULT_TEAM_STATE.copy()

    # TEAM DATA

    home = team_states[
        home_team
    ]

    away = team_states[
        away_team
    ]

    # FEATURE VECTOR

    features = pd.DataFrame([{

        'elo_diff':

            home['elo']
            -
            away['elo'],

        'home_winrate_last_5':

            home['winrate_last_5'],

        'away_winrate_last_5':

            away['winrate_last_5'],

        'home_goals_for_last_5':

            home['goals_for_last_5'],

        'away_goals_for_last_5':

            away['goals_for_last_5'],

        'home_goals_against_last_5':

            home['goals_against_last_5'],

        'away_goals_against_last_5':

            away['goals_against_last_5'],

        'home_goal_diff_last_5':

            home['goal_diff_last_5'],

        'away_goal_diff_last_5':

            away['goal_diff_last_5'],

        'neutral': neutral
    }])

    return features