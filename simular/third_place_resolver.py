def resolve_best_third(

    pattern,
    qualified
):

    allowed_groups = list(
        pattern.replace('3', '')
    )

    candidates = []

    for key, value in (
        qualified.items()
    ):

        if not key.startswith(
            'THIRD'
        ):
            continue

        group_letter = value[
            'group'
        ].replace(
            'Group ',
            ''
        )

        if group_letter in allowed_groups:

            candidates.append(
                value
            )

    candidates = sorted(

        candidates,

        key=lambda x: (

            x['points'],
            x['gd'],
            x['gf']
        ),

        reverse=True
    )

    return candidates[0]['team']