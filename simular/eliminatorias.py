import numpy as np

from simular.ml_match import (
    simulate_ml_match
)

from simular.penalty import (
    simulate_penalty_shootout
)

from simular.state_updater import (
    update_team_states
)


def simulate_knockout_match(

    team_a,
    team_b,

    team_states
):

    (
        outcome,

        home_goals,
        away_goals,

        probs,

        lambda_home,
        lambda_away

    ) = simulate_ml_match(

        team_a,
        team_b,

        team_states
    )

    # EXTRA TIME

    if home_goals == away_goals:

        extra_home = np.random.poisson(
            0.3
        )

        extra_away = np.random.poisson(
            0.3
        )

        home_goals += extra_home
        away_goals += extra_away

    # PENALTIES

    if home_goals == away_goals:

        winner = simulate_penalty_shootout(

            team_a,
            team_b,

            team_states
        )

        penalties = True

    else:

        penalties = False

        if home_goals > away_goals:

            winner = team_a

        else:

            winner = team_b

    # UPDATE STATES

    team_states = update_team_states(

        team_a,
        team_b,

        home_goals,
        away_goals,

        team_states
    )

    result = {

        'team_a': team_a,
        'team_b': team_b,

        'home_goals': home_goals,
        'away_goals': away_goals,

        'winner': winner,

        'penalties': penalties,

        'probs': probs
    }

    return result