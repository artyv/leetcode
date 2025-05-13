import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue = queue.sort_values('turn').reset_index()
    total_weight = 0
    for i in range(queue.shape[0]):
        w = queue.loc[i, 'weight']
        print(i, w)
        if total_weight + w <= 1000:
            total_weight += w
        else:
            return pd.DataFrame({'person_name': [queue.loc[i-1, 'person_name']]})
    return pd.DataFrame({'person_name': [queue.iloc[-1]['person_name']]})