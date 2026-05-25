import math

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


def safe_xg(value):

    # NaN protection

    if value is None:

        return 1.0

    if math.isnan(value):

        return 1.0

    # Prevent negatives

    value = max(
        value,
        0.1
    )

    # Prevent absurd values

    value = min(
        value,
        5.0
    )

    return value


def expected_goals(

    home_team,
    away_team,

    team_states
):

    # NORMALIZE

    home_team = normalize_team_name(
        home_team
    )

    away_team = normalize_team_name(
        away_team
    )

    # FALLBACKS

    if home_team not in team_states:

        print(
            f'WARNING: {home_team} not found in xG model'
        )

        team_states[
            home_team
        ] = DEFAULT_TEAM_STATE.copy()

    if away_team not in team_states:

        print(
            f'WARNING: {away_team} not found in xG model'
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

    # SIMPLE xG MODEL

    home_xg = (

        home['goals_for_last_5']
        * 0.7

        +

        away['goals_against_last_5']
        * 0.3
    )

    away_xg = (

        away['goals_for_last_5']
        * 0.7

        +

        home['goals_against_last_5']
        * 0.3
    )

    # HOME ADVANTAGE

    home_xg += 0.2

    # SANITIZE

    home_xg = safe_xg(
        home_xg
    )

    away_xg = safe_xg(
        away_xg
    )

    return (

        round(home_xg, 2),

        round(away_xg, 2)
    )