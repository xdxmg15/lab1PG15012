import numpy as np

def simulate_match(probs):

    outcomes = [0, 1, 2]

    result = np.random.choice(
        outcomes,
        p=probs
    )

    return result