import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium = stadium[stadium['people'] >= 100].reset_index()
    stadium['id-row_number'] = stadium['id'] - stadium.index
    groups = stadium.groupby("id-row_number")
    size = groups.size()
    valid_groups = size[size >= 3].index
    return stadium[stadium['id-row_number'].isin(valid_groups)][['id', 'visit_date', 'people']]