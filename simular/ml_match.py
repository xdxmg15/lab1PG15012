import numpy as np

from simular.model_loader import (
    model
)

from simular.feature_builder import (
    build_match_features
)

from modelos.gol import (
    expected_goals
)

from simular.poison import (
    poisson_goals
)


def simulate_ml_match(

    home_team,
    away_team,

    team_states
):

    features = build_match_features(

        home_team,
        away_team,

        team_states
    )

    probs = model.predict_proba(
        features
    )[0]

    # Expected goals

    lambda_home, lambda_away = (

        expected_goals(

            home_team,
            away_team,

            team_states
        )
    )

    # Generate goals

    home_goals = poisson_goals(
        lambda_home
    )

    away_goals = poisson_goals(
        lambda_away
    )

    # Derive outcome from goals

    if home_goals > away_goals:

        outcome = 0

    elif away_goals > home_goals:

        outcome = 2

    else:

        outcome = 1

    return (

        outcome,

        home_goals,

        away_goals,

        probs,

        lambda_home,

        lambda_away
    )