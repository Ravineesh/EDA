import numpy as np
import pandas as pd
import streamlit as st

@st.cache
def load_csv(file):
    csv = pd.read_csv(file)
    return csv

def get_null_columns(df):
    cols = ['col_name', 'total_missing_values', '% of missing values', 'col_datatype']
    na_cols = [(col, df[col].isna().sum(),
                np.round(np.divide(df[col].isna().sum(), len(df[col])), 4) * 100,
                df[col].dtype) for col in df.columns
               if df[col].isna().sum() > 0]

    na_cols_df = pd.DataFrame(na_cols, columns=cols)
    na_cols_df = na_cols_df.astype(str)

    return na_cols_df

