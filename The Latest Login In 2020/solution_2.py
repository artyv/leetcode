import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    logins = logins[logins['time_stamp'].dt.year == 2020].rename(columns={'time_stamp': 'last_stamp'})

    groups = logins.groupby('user_id', as_index=False)['last_stamp'].max()

    return groups