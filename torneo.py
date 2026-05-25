from simular.world_cup_loader import (

    load_world_cup_schedule,

    get_groups
)

from simular.grupos_stage import (
    simulate_group
)

from simular.eliminatorias import (
    simulate_knockout_match
)

from simular.build_team_states import (
    build_team_states
)
from simular.qualification import (
    get_group_qualifiers
)

from simular.knockout_bracket import (
    build_round_of_32
)
from simular.bracket_resolver import (
    resolve_team_slot
)

from simular.world_cup_loader import (
    get_round_of_32_matches
)

import copy


group_tables = {}

team_states = build_team_states()

schedule = load_world_cup_schedule()

GROUPS = get_groups(
    schedule
)

# GROUP STAGE

for group_name, teams in GROUPS.items():

    print('\n')

    print(
        f'GROUP {group_name}'
    )

    table = simulate_group(teams)

    print(table)

for group_name, teams in GROUPS.items():

    table = simulate_group(
        teams
    )

    group_tables[
        group_name
    ] = table
    
qualified = get_group_qualifiers(
    group_tables
)
round32_matches = (
    get_round_of_32_matches(
        schedule
    )
)
# ROUND OF 16

print('\n')
print('ROUND OF 16')

matches = [

    ('A1', 'B2'),

    ('B1', 'A2')
]

quarterfinalists = []

for a, b in matches:

    team_a = qualified[a]
    team_b = qualified[b]

    result = simulate_knockout_match(

        team_a,
        team_b,

        team_states
    )

    print(
        f"{team_a} "
        f"{result['home_goals']}"
        f"-"
        f"{result['away_goals']} "
        f"{team_b}"
    )

    print(
        'Winner:',
        result['winner']
    )

    if result['penalties']:

        print(
            '(Penalties)'
        )

    quarterfinalists.append(
        result['winner']
    )

print('\n')
print('QUARTERFINALISTS')

print(quarterfinalists)