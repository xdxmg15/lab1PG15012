def get_match_result(row):

    if row['home_score'] > row['away_score']:
        return 0

    elif row['home_score'] < row['away_score']:
        return 2

    return 1