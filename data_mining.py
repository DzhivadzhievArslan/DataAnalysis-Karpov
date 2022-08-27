import pandas as pd

def get_df_shape(file_path):
    df = pd.read_csv(file_path)
    return df.shape

def get_df_dtypes(file_path):
    df = pd.read_csv(file_path)
    return df.dtypes
