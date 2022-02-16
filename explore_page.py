import streamlit as st
import pandas as pd
import numpy as np

@st.cache
def get_data():
    df = pd.read_csv('data\explore_page_data.csv')
    return df

df = get_data()

st.title('Development Applications in the City of Toronto')

col1, col2, col3, col4 = st.columns(4)

with col1:
    status = st.multiselect("Status", df.Status.unique(),
    default=df.Status.unique())

with col2:
    council = st.multiselect("Council", df.Council.unique(),
    default=df.Council.unique())

with col3:
    consent = st.selectbox("Consent", ('Yes','No'))

if consent == 'Yes':
    consent = 1
else: 
    consent = 0

with col4:
    minor_variance = st.selectbox("Minor Variance", ('Yes','No'))

if minor_variance == 'Yes':
    minor_variance = 1
else: 
    minor_variance = 0

#Query the data based on the user parameters
df_selection = df.query("Status == @status & Council == @council & Consent == @consent & Minor_Variance == @minor_variance" )

st.map(df_selection)
st.write(df_selection)