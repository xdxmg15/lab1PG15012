from joblib import load
import pandas as pd


model = load(
    'modelos/world_cup_model.joblib'
)

sample = pd.DataFrame([{

    'elo_diff': 50,

    'home_winrate_last_5': 0.8,
    'away_winrate_last_5': 0.4,

    'home_goals_for_last_5': 2.1,
    'away_goals_for_last_5': 1.0,

    'home_goals_against_last_5': 0.6,
    'away_goals_against_last_5': 1.4,

    'home_goal_diff_last_5': 1.5,
    'away_goal_diff_last_5': -0.4,

    'neutral': 1
}])

probs = model.predict_proba(sample)

print(probs)