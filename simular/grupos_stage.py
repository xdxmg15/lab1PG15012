import itertools
import copy
from simular.state_updater import (
    update_team_states
)
from simular.standings import (

    create_empty_table,
    update_table,
    sort_table
)

from simular.ml_match import (
    simulate_ml_match
)

from simular.build_team_states import (
    build_team_states
)


def simulate_group(group_teams):

    team_states = build_team_states()

    table = create_empty_table(
        group_teams
    )

    fixtures = list(

        itertools.combinations(
            group_teams,
            2
        )
    )

    for home, away in fixtures:

        (
            outcome,

            home_goals,
            away_goals,

            probs,

            lambda_home,
            lambda_away

        ) = simulate_ml_match(

            home,
            away,

            team_states
        )

        print(
            f'{home} {home_goals}-{away_goals} {away}'
        )

        print(
            f'xG: {lambda_home:.2f} - {lambda_away:.2f}'
        )

        print(
            'Probabilities:',
            probs
        )

        table = update_table(

            table,

            home,
            away,

            home_goals,
            away_goals
        )
        team_states = update_team_states(

            home,
            away,

            home_goals,
            away_goals,

            team_states
        )

    table = sort_table(table)

    return table