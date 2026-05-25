from simular.mundial import (
    simulate_world_cup
)

from simular.stats_tracker import (
    StatsTracker
)


SIMULATIONS = 1000000

stats = StatsTracker()

for sim in range(SIMULATIONS):

    result = simulate_world_cup()

    stats.update(result)

    if sim % 100 == 0:

        print(
            f'Simulation {sim}'
        )

print('\n')
print('WORLD CUP 2026 PROBABILITIES')
print('\n')

champion_probs = []

for team, wins in (
    stats.champions.items()
):

    probability = (
        wins / SIMULATIONS
    )

    champion_probs.append(
        (team, probability)
    )

champion_probs = sorted(

    champion_probs,

    key=lambda x: x[1],

    reverse=True
)

for team, prob in champion_probs:

    print(
        f'{team}: {prob:.2%}'
    )