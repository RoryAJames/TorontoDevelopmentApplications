from sklearn import neighbors
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

col1, col2, col3 = st.columns(3)

with col1:
    status = st.radio("Status", df.Status.unique())

with col2:
    council = st.radio("Council", df.Council.unique())

with col3:
    consent = st.radio("Consent", df.Consent.unique())


df = df[df['Status'] == status]
df = df[df['Council'] == council]
df = df[df['Consent'] == consent]

st.map(df)
st.write(df)