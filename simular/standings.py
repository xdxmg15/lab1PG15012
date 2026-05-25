import pandas as pd


def create_empty_table(teams):

    table = pd.DataFrame({

        'team': teams,

        'points': 0,

        'gf': 0,

        'ga': 0,

        'gd': 0,

        'wins': 0,

        'draws': 0,

        'losses': 0
    })

    return table


def update_table(
    table,
    home,
    away,
    home_goals,
    away_goals
):

    # HOME

    table.loc[
        table['team'] == home,
        'gf'
    ] += home_goals

    table.loc[
        table['team'] == home,
        'ga'
    ] += away_goals

    # AWAY

    table.loc[
        table['team'] == away,
        'gf'
    ] += away_goals

    table.loc[
        table['team'] == away,
        'ga'
    ] += home_goals

    # GOAL DIFF

    table['gd'] = (
        table['gf']
        -
        table['ga']
    )

    # RESULT

    if home_goals > away_goals:

        table.loc[
            table['team'] == home,
            'points'
        ] += 3

        table.loc[
            table['team'] == home,
            'wins'
        ] += 1

        table.loc[
            table['team'] == away,
            'losses'
        ] += 1

    elif away_goals > home_goals:

        table.loc[
            table['team'] == away,
            'points'
        ] += 3

        table.loc[
            table['team'] == away,
            'wins'
        ] += 1

        table.loc[
            table['team'] == home,
            'losses'
        ] += 1

    else:

        table.loc[
            table['team'] == home,
            'points'
        ] += 1

        table.loc[
            table['team'] == away,
            'points'
        ] += 1

        table.loc[
            table['team'] == home,
            'draws'
        ] += 1

        table.loc[
            table['team'] == away,
            'draws'
        ] += 1

    return table


def sort_table(table):

    table = table.sort_values(

        by=[
            'points',
            'gd',
            'gf',
            'wins'
        ],

        ascending=False

    ).reset_index(drop=True)

    return table