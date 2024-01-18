import pandas as pd

class DataFrameGeneral():

    def __init__(self, df) -> None:
        self.df = df
        self.df_1 = None
        self.df_2 = None


class DataFrameModif(DataFrameGeneral):
    pass

class DataFrameFilter(DataFrameGeneral):
    pass