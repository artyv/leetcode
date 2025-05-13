import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [len(players.iloc[:, 0]), len(players.iloc[0])]