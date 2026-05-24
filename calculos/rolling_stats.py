import pandas as pd

def create_team_stats(results):

    home_df = pd.DataFrame({
        'date': results['date'],
        'team': results['home_team'],
        'opponent': results['away_team'],
        'goals_for': results['home_score'],
        'goals_against': results['away_score'],
        'is_home': 1
    })

    away_df = pd.DataFrame({
        'date': results['date'],
        'team': results['away_team'],
        'opponent': results['home_team'],
        'goals_for': results['away_score'],
        'goals_against': results['home_score'],
        'is_home': 0
    })

    team_stats = pd.concat(
        [home_df, away_df],
        ignore_index=True
    )

    team_stats = team_stats.sort_values(
        ['team', 'date']
    )

    return team_stats


def add_form_features(team_stats):

    team_stats['win'] = (
        team_stats['goals_for']
        >
        team_stats['goals_against']
    ).astype(int)

    team_stats['draw'] = (
        team_stats['goals_for']
        ==
        team_stats['goals_against']
    ).astype(int)

    team_stats['loss'] = (
        team_stats['goals_for']
        <
        team_stats['goals_against']
    ).astype(int)

    team_stats['winrate_last_5'] = (
        team_stats
        .groupby('team')['win']
        .transform(
            lambda x:
            x.shift(1)
             .rolling(5, min_periods=1)
             .mean()
        )
    )

    team_stats['goals_for_last_5'] = (
        team_stats
        .groupby('team')['goals_for']
        .transform(
            lambda x:
            x.shift(1)
             .rolling(5, min_periods=1)
             .mean()
        )
    )

    team_stats['goals_against_last_5'] = (
        team_stats
        .groupby('team')['goals_against']
        .transform(
            lambda x:
            x.shift(1)
             .rolling(5, min_periods=1)
             .mean()
        )
    )

    team_stats['goal_diff_last_5'] = (
        team_stats['goals_for_last_5']
        -
        team_stats['goals_against_last_5']
    )

    return team_stats