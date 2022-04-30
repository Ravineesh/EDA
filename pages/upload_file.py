import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
from pages import config
import io
import streamlit as st


# from streamlit_lottie import st_lottie


# @st.cache
def app():
    # Upload the dataset and save as csv
    st.write("\n")

    # upload the csv file:
    upload_file = st.file_uploader(config.file_upload_label, type=["csv"])
    # define global variable
    global main_dataframe
    if upload_file is None:
        st.info(config.file_upload_info)
        st.stop()
    else:
        main_dataframe = utils.load_csv(upload_file)

    if 'key' not in st.session_state:
        st.session_state['dataframe'] = main_dataframe

    ''' Load the data and save the columns with categories as a dataframe. 
    This section also allows changes in the numerical and categorical columns. '''
    load = st.button('Load Data', help="This will save the copy of your data for further analysis")

    if load:
        main_dataframe.to_csv('data/main_data.csv', index=False)
        # df = pd.read_csv('data/main_data.csv')
        df = st.session_state['dataframe']
        st.write('Dataframe Loaded')
        st.dataframe(df)
