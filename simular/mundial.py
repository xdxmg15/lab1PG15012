from simular.grupos_stage import (
    simulate_group
)

from simular.eliminatorias import (
    simulate_knockout_match
)

from simular.build_team_states import (
    build_team_states
)

from simular.world_cup_loader import (

    load_world_cup_schedule,

    get_groups,

    get_round_of_32_matches
)

from simular.qualification import (
    get_group_qualifiers
)

from simular.bracket_resolver import (
    resolve_team_slot
)


def play_knockout_round(

    teams,
    team_states
):

    winners = []

    for i in range(
        0,
        len(teams),
        2
    ):

        result = simulate_knockout_match(

            teams[i],
            teams[i + 1],

            team_states
        )

        winners.append(
            result['winner']
        )

    return winners


def simulate_world_cup():

    # LOAD DATA

    team_states = build_team_states()

    schedule = load_world_cup_schedule()

    GROUPS = get_groups(
        schedule
    )

    # GROUP STAGE

    group_tables = {}

    for group_name, teams in (
        GROUPS.items()
    ):

        table = simulate_group(
            teams
        )

        group_tables[
            group_name
        ] = table

    # QUALIFICATION

    qualified = get_group_qualifiers(
        group_tables
    )

    # ROUND OF 32

    round32_matches = (
        get_round_of_32_matches(
            schedule
        )
    )

    round16_teams = []

    for slot_a, slot_b in (
        round32_matches
    ):

        team_a = resolve_team_slot(

            slot_a,
            qualified
        )

        team_b = resolve_team_slot(

            slot_b,
            qualified
        )

        result = simulate_knockout_match(

            team_a,
            team_b,

            team_states
        )

        round16_teams.append(
            result['winner']
        )

    # ROUND OF 16

    quarterfinalists = play_knockout_round(

        round16_teams,

        team_states
    )

    # QUARTERFINALS

    semifinalists = play_knockout_round(

        quarterfinalists,

        team_states
    )

    # SEMIFINALS

    finalists = play_knockout_round(

        semifinalists,

        team_states
    )

    # FINAL

    final_result = simulate_knockout_match(

        finalists[0],
        finalists[1],

        team_states
    )

    champion = final_result[
        'winner'
    ]

    return {

        'champion': champion,

        'finalists': finalists,

        'semifinalists':
            semifinalists,

        'quarterfinalists':
            quarterfinalists,

        'round16':
            round16_teams,

        'qualified':
            qualified
    }