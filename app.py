import streamlit as st
import pandas as pd
import numpy as np

@st.cache
def get_data():
    df = pd.read_excel('data/combined_files_output.xlsx')
    df = df.rename(columns={'Latitude':'lat','Longitude':'lon'})
    return df

df = get_data()

st.title('Development Applications in the City of Toronto')
st.markdown('Welcome to this interactive app that allows users to explore development application in the City of Toronto')

status = st.sidebar.radio("Status", df.Status.unique())
council = st.sidebar.radio("Council", df.Council.unique())
num_properties = st.sidebar.radio("Number of Properties", df.Number_of_Properties.unique())
application_choice = st.sidebar.multiselect("Application Type",['Consent','Minor Variance', 'Official Plan Rezoning', 'Site Plan Application'])

st.map(df)