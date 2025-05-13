import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    categories = pd.DataFrame({'category': ['Low Salary', 'Average Salary', 'High Salary']})

    accounts['category'] = pd.cut(
        accounts['income'],
        bins=[-float('inf'), 20000, 50000, float('inf')],
        labels=['Low Salary', 'Average Salary', 'High Salary']
    )
    
    grouped = accounts.groupby('category', as_index=False).count().rename(columns={'income': 'accounts_count'})

    merged = categories.merge(grouped, how='left', on='category').fillna(0)

    return merged[['category', 'accounts_count']]