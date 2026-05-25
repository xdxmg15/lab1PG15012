def build_round_of_32(

    qualified
):

    group_winners = []
    runners_up = []
    best_thirds = []

    for key, value in (
        qualified.items()
    ):

        if key.endswith('_1'):

            group_winners.append(
                value['team']
            )

        elif key.endswith('_2'):

            runners_up.append(
                value['team']
            )

        elif key.startswith('THIRD'):

            best_thirds.append(
                value['team']
            )

    round32 = []

    # WINNERS vs THIRDS

    for i in range(

        min(
            len(group_winners),
            len(best_thirds)
        )
    ):

        round32.append(

            (
                group_winners[i],
                best_thirds[i]
            )
        )

    # RUNNERS vs RUNNERS

    remaining = runners_up.copy()

    while len(remaining) >= 2:

        team_a = remaining.pop(0)

        team_b = remaining.pop(0)

        round32.append(
            (team_a, team_b)
        )

    return round32