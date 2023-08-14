# classes.py
class Dataset:
    def __init__(self, path: str = "./data/nfl_offensive_stats.csv"):
        from pandas import read_csv
        self.path = path
        self.data = read_csv(self.path).rename(columns={'position ': 'position'}, inplace=True)

        






















# app.py

from classes import Dataset


df = Dataset().data





# testing.py

from classes import Dataset

def check_that_column_is_renamed_correctly(df):
    SPACED_COLUMN_NOT_IN_DF = ("position " not in df.columns())
    CLEANED_COLUMN_IS_IN_DF = ("position" in df.columns())
    
    # assert SPACED_COLUMN_NOT_IN_DF, "ERROR: Spaced column actually exists in dataframe!"
    # assert CLEANED_COLUMN_IS_IN_DF, "ERROR: Expected cleaned column actually not in dataframe!"
    
    try:
        len(df["position"])
    except:
        print("Test failed: `position` does not exist in dataframe.")
    finally:
        print(f"Current columns in dataframe: {df.columns()}")
    
df = Dataset().data

check_that_column_is_renamed_correctly(df)  # Should return nothing and pass
