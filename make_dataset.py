import pandas as pd

from calculos.cargar import cargar
from calculos.target import get_match_result
from calculos.rolling_stats import (
    create_team_stats,
    add_form_features
)

from calculos.elo import calculate_elo


results = cargar(
    'csv/results.csv'
)

results['target'] = results.apply(
    get_match_result,
    axis=1
)

results = calculate_elo(results)

team_stats = create_team_stats(results)

team_stats = add_form_features(
    team_stats
)

home_features = team_stats[
    [
        'date',
        'team',
        'winrate_last_5',
        'goals_for_last_5',
        'goals_against_last_5',
        'goal_diff_last_5'
    ]
].copy()

home_features.columns = [
    'date',
    'home_team',
    'home_winrate_last_5',
    'home_goals_for_last_5',
    'home_goals_against_last_5',
    'home_goal_diff_last_5'
]

away_features = team_stats[
    [
        'date',
        'team',
        'winrate_last_5',
        'goals_for_last_5',
        'goals_against_last_5',
        'goal_diff_last_5'
    ]
].copy()

away_features.columns = [
    'date',
    'away_team',
    'away_winrate_last_5',
    'away_goals_for_last_5',
    'away_goals_against_last_5',
    'away_goal_diff_last_5'
]

results = results.merge(
    home_features,
    on=['date', 'home_team'],
    how='left'
)

results = results.merge(
    away_features,
    on=['date', 'away_team'],
    how='left'
)

features = [

    'elo_diff',

    'home_winrate_last_5',
    'away_winrate_last_5',

    'home_goals_for_last_5',
    'away_goals_for_last_5',

    'home_goals_against_last_5',
    'away_goals_against_last_5',

    'home_goal_diff_last_5',
    'away_goal_diff_last_5',

    'neutral'
]

dataset = results.dropna(
    subset=features
)

dataset.to_csv(
    'csv/resultado/dataset.csv',
    index=False
)

print(dataset[features].head())

print(dataset['target'].value_counts())

print(dataset.shape)

print(
    'Dataset generado correctamente.'
)