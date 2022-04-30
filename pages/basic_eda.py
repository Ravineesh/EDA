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
    df = st.session_state['dataframe']

    # preview of dataset
    st.subheader('Preview of dataset:')
    with st.expander('Click here to view top 10 rows'):
        st.info(f'Number of rows: {df.shape[0]}, Number of columns: {df.shape[1]}')
        st.dataframe(df.head(10))
    with st.expander('Click here to view bottom 10 rows'):
        st.info(f'Number of rows: {df.shape[0]}, Number of columns: {df.shape[1]}')
        st.dataframe(df.tail(10))
    with st.expander('Click here to view the entire dataset'):
        st.info(f'Number of rows: {df.shape[0]}, Number of columns: {df.shape[1]}')
        st.dataframe(df)

    # information about columns (counting part)
    st.subheader('Columns Datatype info:')
    with st.expander('Click here to columns data types'):
        # columns_types = get_columns_types(df)
        object_type, int_type, float_type, bool_type, date_time, time_delta, category = st.columns(7)
        object_type.metric('Object', 2)
        int_type.metric('Integer', 2)
        float_type.metric('Float ', 2)
        bool_type.metric('Boolean', 2)
        date_time.metric('Date_time', 2)
        time_delta.metric('Date_time_delta', 2)
        category.metric('Category', 2)

    # pandas describe
    st.subheader('Pandas describe')
    with st.expander('Click here to view pandas describe output'):
        st.dataframe(df.describe())

    # pandas info
    st.subheader('Pandas info')
    with st.expander('Click here to view pandas info output'):
        buffer = io.StringIO()
        df.info(buf=buffer)
        df_info = buffer.getvalue()
        st.text(df_info)

    # Columns having null values
    st.subheader('Columns having Null Values')
    with st.expander('Click here to view the columns having null values'):
        null_columns = utils.get_null_columns(df)
        if len(null_columns) == 0:
            st.info('Lucky you....your dataset do not have any columns having null values!')
        elif len(null_columns) == 1:
            st.info(f'There is only 1 column out of {df.shape[1]} columns having null value!')
            st.dataframe(null_columns)
        else:
            st.info(
                f'There are total {len(null_columns)} out of {df.shape[1]} columns which are having '
                f'null values!')
            st.dataframe(null_columns)

    # Duplicate columns
    st.subheader('Duplicate Rows')
    with st.expander('Click here to view the duplicate rows'):
        duplicate_df = df[df.duplicated(keep='first')]
        if len(duplicate_df) == 0:
            st.info('Lucky you....your dataset do not have any duplicate rows!')
        else:
            st.info(f'There are total {len(duplicate_df)} duplicate rows out of {len(df)} original rows')
            st.dataframe(duplicate_df)

    # Duplicate columns
    st.subheader('Groupby Operations Rows')
    with st.expander('Click here to perform group by operation'):
        st.write('Groupby')
        df_columns = df.columns
        group_by = st.selectbox(label='Select the 1st column', options=df_columns)
        
        performed_on = st.selectbox(label='Select the 2nd column', options=df_columns)
        operation = st.selectbox(label='Select operation', options=['sum', 'count'])
        run_query = st.button(label='Run Query')
        if run_query:
            if operation == 'sum':
                result = df.groupby(group_by)[f'{performed_on}'].sum()
                st.dataframe(result)
            if operation == 'count':
                result = result = df.groupby(group_by)[f'{performed_on}'].count()
                st.dataframe(result)