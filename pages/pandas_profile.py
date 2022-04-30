import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport


def app():
    # Upload the dataset and save as csv
    profile_df = pd.read_csv('data/main_data.csv')
    print(type(profile_df))
    df_profile = ProfileReport(profile_df, explorative=False)
    st_profile_report(df_profile)
