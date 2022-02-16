import streamlit as st
import pandas as pd
import numpy as np

@st.cache
def get_data():
    df = pd.read_csv('data\explore_page_data.csv')
    return df

df = get_data()

st.title('Development Applications in the City of Toronto')
st.markdown("""This interactive dashboard is designed for visualizing development applications in the City of Toronto. Specifically, the intent of the dashboard is to give users the
functionality to visualize applications based on their decision status, and the various parameters of the applications. All of the data for this project was sourced from
 the [City of Toronto Open Data Portal](https://open.toronto.ca/).
""")

##Row 1

row1_col1, row1_col2 = st.columns([0.6, 2])

with row1_col1:
    status = st.selectbox("Status", df.Status.unique())
    
with row1_col2:
    council = st.multiselect("Council", df.Council.unique(),
    default=df.Council.unique())

 ## Row 2   

row2_col1, row2_col2, row2_col3 = st.columns([0.6, 1.4, 2])

with row2_col1:
    consent = st.selectbox("Consent", ('Yes','No'))

if consent == 'Yes':
    consent = 1
else: 
    consent = 0

with row2_col2:
    minor_variance = st.selectbox("Minor Variance", ('Yes','No'))

if minor_variance == 'Yes':
    minor_variance = 1
else: 
    minor_variance = 0

#Query the data based on the user parameters
df_selection = df.query("Status == @status & Council == @council & Consent == @consent & Minor_Variance == @minor_variance")

st.map(df_selection)
st.write(df_selection)