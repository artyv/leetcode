import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    categories = pd.DataFrame({'category': ['Low Salary', 'Average Salary', 'High Salary']})

    for i in range(accounts.shape[0]):
        salary = accounts.loc[i, 'income']
        if salary < 20000:
            accounts.loc[i, 'category'] = 'Low Salary'
        elif salary <= 50000:
            accounts.loc[i, 'category'] = 'Average Salary'
        else:
            accounts.loc[i, 'category'] = 'High Salary'
    
    merged = categories.merge(accounts[['category', 'income']], how='left', on='category')
    grouped = merged.groupby('category', as_index=False).count().rename(columns={'income': 'accounts_count'})

    return grouped