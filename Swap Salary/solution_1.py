import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    for i in range(len(salary)):
        salary['sex'][i] = 'm' if salary['sex'][i] == 'f' else 'f'
    return salary