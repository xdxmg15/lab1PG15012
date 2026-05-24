import pandas as pd

from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score,
    log_loss
)

from joblib import dump


dataset = pd.read_csv(
    'data/processed/dataset.csv'
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

target = 'target'

train = dataset[
    dataset['date'] < '2022-01-01'
]

test = dataset[
    dataset['date'] >= '2022-01-01'
]

X_train = train[features]
y_train = train[target]

X_test = test[features]
y_test = test[target]

model = XGBClassifier(

    objective='multi:softprob',

    num_class=3,

    n_estimators=300,

    max_depth=6,

    learning_rate=0.03,

    subsample=0.8,

    colsample_bytree=0.8,

    eval_metric='mlogloss'
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

probs = model.predict_proba(X_test)

print(
    'Accuracy:',
    accuracy_score(y_test, predictions)
)

print(
    'Log Loss:',
    log_loss(y_test, probs)
)

dump(
    model,
    'models/world_cup_model.joblib'
)

print('Modelo guardado.')