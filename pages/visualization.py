import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from pages import utils
import matplotlib.pyplot as plt
import seaborn as sns
import os


def app():
    df_viz = pd.read_csv('data/main_data.csv')
    target_column = st.selectbox(label='Select the target column', options=df_viz.columns)
    st.subheader('Pie Chart')
    pie_chart = px.pie(data_frame=df_viz, names=target_column)
    st.plotly_chart(pie_chart)
    st.subheader('Bar Chart')
    bar_chart = px.bar(data_frame=df_viz, x=target_column)
    st.plotly_chart(bar_chart)
