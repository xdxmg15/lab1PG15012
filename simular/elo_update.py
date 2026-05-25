def update_elo(

    home_elo,
    away_elo,

    home_goals,
    away_goals,

    k=20
):

    expected_home = 1 / (

        1 +

        10 ** (
            (away_elo - home_elo) / 400
        )
    )

    if home_goals > away_goals:

        actual_home = 1

    elif home_goals < away_goals:

        actual_home = 0

    else:

        actual_home = 0.5

    new_home_elo = (

        home_elo

        +

        k * (
            actual_home - expected_home
        )
    )

    new_away_elo = (

        away_elo

        +

        k * (
            (1 - actual_home)
            -
            (1 - expected_home)
        )
    )

    return (

        new_home_elo,
        new_away_elo
    )