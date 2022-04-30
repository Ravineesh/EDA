import os
import streamlit as st
import numpy as np
from PIL import Image
from pages import config

# Custom imports
from multipage import MultiPage
from pages import upload_file, basic_eda, pandas_profile, visualization

# set the layout of app
st.set_page_config(layout=config.layout, page_title=config.title)

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title(config.title)

# about section
with st.expander('About this app'):
    st.write(config.about_app)


# Add all your application here
app.add_page("Upload File", upload_file.app)
app.add_page("Basic Analysis", basic_eda.app)
app.add_page("Pandas Profiling", pandas_profile.app)
app.add_page("Data Visualization", visualization.app)

# The main app
app.run()
