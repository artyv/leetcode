import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(transactions[['account', 'amount']], users, how='left', on='account')
    res = merged.groupby('name', as_index=False)['amount'].sum().rename(columns={'amount':'balance'})
    return res[res['balance'] > 10000]