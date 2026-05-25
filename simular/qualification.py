import pandas as pd


def get_group_qualifiers(

    group_tables
):

    qualified = {}

    third_place_teams = []

    for group_name, table in (
        group_tables.items()
    ):

        # EXTRACT LETTER

        group_letter = (
            group_name
            .replace('Group ', '')
            .strip()
        )

        # FIRST PLACE

        qualified[
            f'1{group_letter}'
        ] = {

            'team':
                table.iloc[0]['team'],

            'group':
                group_name,

            'points':
                table.iloc[0]['points'],

            'gd':
                table.iloc[0]['gd'],

            'gf':
                table.iloc[0]['gf']
        }

        # SECOND PLACE

        qualified[
            f'2{group_letter}'
        ] = {

            'team':
                table.iloc[1]['team'],

            'group':
                group_name,

            'points':
                table.iloc[1]['points'],

            'gd':
                table.iloc[1]['gd'],

            'gf':
                table.iloc[1]['gf']
        }

        # THIRD PLACE

        third_place_teams.append({

            'team':
                table.iloc[2]['team'],

            'group':
                group_letter,

            'points':
                table.iloc[2]['points'],

            'gd':
                table.iloc[2]['gd'],

            'gf':
                table.iloc[2]['gf']
        })

    # SORT THIRD PLACES

    third_df = pd.DataFrame(
        third_place_teams
    )

    third_df = third_df.sort_values(

        by=[
            'points',
            'gd',
            'gf'
        ],

        ascending=False
    )

    # BEST 8 THIRDS

    best_thirds = third_df.head(8)

    for idx, row in (
        best_thirds.iterrows()
    ):

        qualified[
            f'THIRD_{idx}'
        ] = {

            'team':
                row['team'],

            'group':
                row['group'],

            'points':
                row['points'],

            'gd':
                row['gd'],

            'gf':
                row['gf']
        }

    return qualified