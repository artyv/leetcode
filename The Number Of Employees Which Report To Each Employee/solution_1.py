import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employees[['employee_id', 'name']], employees[['employee_id', 'reports_to', 'age']], how='inner', left_on='employee_id', right_on='reports_to')
    merged = merged.drop('reports_to', axis='columns')
    merged = merged.rename(columns={'employee_id_x': 'employee_id', 'employee_id_y': 'reports_count', 'age': 'average_age'})

    grouped = merged.groupby(['employee_id', 'name'])
    
    res = grouped.agg({'reports_count': 'count', 'average_age':'mean'}).reset_index()
    res['average_age'] = (res['average_age'] + 0.001).round()

    return res