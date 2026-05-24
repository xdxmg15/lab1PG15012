import pandas as pd

def cargar(path):

    results = pd.read_csv(
        path,
        parse_dates=['date']
    )

    results = results.sort_values(
        'date'
    ).reset_index(drop=True)

    return results