import random

from simular.team_utils import (
    normalize_team_name
)

DEFAULT_ELO = 1500


def simulate_penalty_shootout(

    team_a,
    team_b,

    team_states
):

    # NORMALIZE

    team_a = normalize_team_name(
        team_a
    )

    team_b = normalize_team_name(
        team_b
    )

    # SAFE ELO FETCH

    elo_a = team_states.get(

        team_a,

        {'elo': DEFAULT_ELO}
    )['elo']

    elo_b = team_states.get(

        team_b,

        {'elo': DEFAULT_ELO}
    )['elo']

    # ELO ADVANTAGE

    prob_a = (

        1
        /
        (
            1
            +
            10 ** (
                (elo_b - elo_a)
                / 400
            )
        )
    )

    # RANDOM PENALTIES

    if random.random() < prob_a:

        return team_a

    return team_b