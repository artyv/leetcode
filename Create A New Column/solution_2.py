import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[:, 'bonus'] = employees['salary'] * 2
    return employees