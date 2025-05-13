import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    ids = employees['employee_id']
    names = employees['name']
    salaries = employees['salary']
    bonus = pd.Series([0]*len(names))

    for i in range(len(names)):
        if ids[i] % 2 == 1 and names[i][0] != 'M':
            bonus[i] = salaries[i]
    employees['bonus'] = bonus
    return employees[['employee_id', 'bonus']]