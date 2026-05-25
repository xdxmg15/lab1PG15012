import numpy as np
import math


def poisson_goals(

    lambda_value
):

    # SAFETY

    if lambda_value is None:

        lambda_value = 1.0

    if math.isnan(lambda_value):

        lambda_value = 1.0

    lambda_value = max(
        lambda_value,
        0.1
    )

    lambda_value = min(
        lambda_value,
        6.0
    )

    goals = np.random.poisson(
        lam=lambda_value
    )

    return int(goals)