def calculate_elo(results):

    INITIAL_ELO = 1500
    K = 20

    elo_dict = {}

    home_elo_list = []
    away_elo_list = []

    for idx, row in results.iterrows():

        home = row['home_team']
        away = row['away_team']

        home_elo = elo_dict.get(
            home,
            INITIAL_ELO
        )

        away_elo = elo_dict.get(
            away,
            INITIAL_ELO
        )

        home_elo_list.append(home_elo)
        away_elo_list.append(away_elo)

        expected_home = 1 / (
            1 + 10 ** (
                (away_elo - home_elo) / 400
            )
        )

        if row['home_score'] > row['away_score']:
            actual_home = 1

        elif row['home_score'] < row['away_score']:
            actual_home = 0

        else:
            actual_home = 0.5

        new_home_elo = (
            home_elo +
            K * (
                actual_home - expected_home
            )
        )

        new_away_elo = (
            away_elo +
            K * (
                (1 - actual_home)
                -
                (1 - expected_home)
            )
        )

        elo_dict[home] = new_home_elo
        elo_dict[away] = new_away_elo

    results['home_elo'] = home_elo_list
    results['away_elo'] = away_elo_list

    results['elo_diff'] = (
        results['home_elo']
        -
        results['away_elo']
    )

    return results