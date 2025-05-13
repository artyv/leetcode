import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    aux = rides.groupby(['user_id'])['distance'].sum().reset_index(name='travelled_distance')
    aux = pd.merge(users, aux, how='left', left_on='id', right_on='user_id').drop(['id', 'user_id'], axis='columns')
    aux['travelled_distance'] = aux['travelled_distance'].fillna(0)
    aux = aux.sort_values(by=['travelled_distance', 'name'], ascending=[False, True])
    return aux
