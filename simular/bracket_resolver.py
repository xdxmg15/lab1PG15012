from simular.third_place_resolver import (
    resolve_best_third
)


def resolve_team_slot(

    slot,
    qualified
):

    # THIRD PLACE SLOT

    if slot.startswith('3'):

        return resolve_best_third(

            slot,
            qualified
        )

    # GROUP WINNER / RUNNER

    if slot in qualified:

        return qualified[
            slot
        ]['team']

    raise ValueError(
        f'Unknown slot: {slot}'
    )