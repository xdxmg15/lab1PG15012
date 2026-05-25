import pandas as pd
import os


def load_world_cup_schedule():

    script_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    csv_path = os.path.join(

        script_dir,
        '..',
        'csv',
        'fifa-world-cup-2026-UTC.csv'
    )

    df = pd.read_csv(csv_path)

    return df


def get_all_teams(schedule_df):

    home_teams = set(
        schedule_df['Home Team']
    )

    away_teams = set(
        schedule_df['Away Team']
    )

    teams = sorted(

        list(
            home_teams.union(
                away_teams
            )
        )
    )

    return teams


def get_groups(schedule_df):

    groups = {}

    group_stage = schedule_df[

        schedule_df['Group']
        .astype(str)
        .str.contains('Group')
    ]

    for group_name in sorted(
        group_stage['Group'].unique()
    ):

        group_matches = group_stage[

            group_stage['Group']
            ==
            group_name
        ]

        teams = set(
            group_matches['Home Team']
        ).union(

            set(
                group_matches['Away Team']
            )
        )

        groups[group_name] = sorted(
            list(teams)
        )

    return groups

def get_round_of_32_matches(

    schedule_df
):

    round32 = schedule_df[

        schedule_df[
            'Round Number'
        ]
        ==
        'Round of 32'
    ]

    matches = []

    for _, row in (
        round32.iterrows()
    ):

        matches.append(

            (

                row['Home Team'],

                row['Away Team']
            )
        )

    return matches