from simular.elo_update import (
    update_elo
)

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


def update_team_states(

    home_team,
    away_team,

    home_goals,
    away_goals,

    team_states
):

    # NORMALIZE NAMES

    home_team = normalize_team_name(
        home_team
    )

    away_team = normalize_team_name(
        away_team
    )

    # FALLBACK STATES

    if home_team not in team_states:

        print(
            f'WARNING: {home_team} missing in update'
        )

        team_states[
            home_team
        ] = DEFAULT_TEAM_STATE.copy()

    if away_team not in team_states:

        print(
            f'WARNING: {away_team} missing in update'
        )

        team_states[
            away_team
        ] = DEFAULT_TEAM_STATE.copy()

    # TEAM OBJECTS

    home = team_states[
        home_team
    ]

    away = team_states[
        away_team
    ]

    # UPDATE ELO

    new_home_elo, new_away_elo = (

        update_elo(

            home['elo'],
            away['elo'],

            home_goals,
            away_goals
        )
    )

    home['elo'] = new_home_elo

    away['elo'] = new_away_elo

    # MATCH RESULT

    if home_goals > away_goals:

        home_result = 1
        away_result = 0

    elif home_goals < away_goals:

        home_result = 0
        away_result = 1

    else:

        home_result = 0.5
        away_result = 0.5

    # EXPONENTIAL MOVING UPDATE

    alpha = 0.30

    # WINRATE

    home['winrate_last_5'] = (

        (1 - alpha)

        * home['winrate_last_5']

        +

        alpha * home_result
    )

    away['winrate_last_5'] = (

        (1 - alpha)

        * away['winrate_last_5']

        +

        alpha * away_result
    )

    # GOALS FOR

    home['goals_for_last_5'] = (

        (1 - alpha)

        * home['goals_for_last_5']

        +

        alpha * home_goals
    )

    away['goals_for_last_5'] = (

        (1 - alpha)

        * away['goals_for_last_5']

        +

        alpha * away_goals
    )

    # GOALS AGAINST

    home['goals_against_last_5'] = (

        (1 - alpha)

        * home['goals_against_last_5']

        +

        alpha * away_goals
    )

    away['goals_against_last_5'] = (

        (1 - alpha)

        * away['goals_against_last_5']

        +

        alpha * home_goals
    )

    # GOAL DIFFERENCE

    home['goal_diff_last_5'] = (

        home['goals_for_last_5']

        -

        home['goals_against_last_5']
    )

    away['goal_diff_last_5'] = (

        away['goals_for_last_5']

        -

        away['goals_against_last_5']
    )

    return team_states