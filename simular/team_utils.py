from simular.team_name_mapping import (
    TEAM_NAME_MAPPING
)


def normalize_team_name(team):

    return TEAM_NAME_MAPPING.get(
        team,
        team
    )