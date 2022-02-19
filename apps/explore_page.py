import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

@st.cache
def get_data():
    df = pd.read_csv('data\explore_page_data.csv')
    return df

df = get_data()

def show_explore_page():

    st.title('Explore Development Applications In The City of Toronto')
    st.write('Note - This dashboard only shows applications based on their status as of May 3rd 2017.')
    st.write('')

##Row 1
    row1_col1, row1_col2, row1_col3 = st.columns([1, 1.5, 2])

    with row1_col1:
        status = st.selectbox("Select The Application Status", df.Status.unique())

    with row1_col2:
        num_props = st.multiselect("Select The Number of Properties", df.Number_of_Properties.unique())
    
    with row1_col3:
        council = st.multiselect("Select The Council(s) Of Interest", df.Council.unique())

 ## Row 2   

    row2_col1, row2_col2 = st.columns([1.8, 1.8])

    with row2_col1:
        application_type = st.multiselect("Select The Application Type(s)", ('Consent','Minor Variance',
        'Official Plan Rezoning', 'Site Plan Application'))

    #Check what has been selected from application type
    
    if 'Consent' in application_type:
        consent = 1
    else:
        consent = 0
    
    if 'Minor Variance' in application_type:
        minor_variance = 1
    else:
        minor_variance = 0

    if 'Official Plan Rezoning' in application_type:
        official_plan = 1
    else:
        official_plan = 0
    
    if 'Site Plan Application' in application_type:
        site_plan = 1
    else:
        site_plan = 0
        
    with row2_col2:
        average_income = st.slider("Show Applications In Range of Neighbourhood Average Income",value=(25000,350000))
        average_income_lower = average_income[0]
        average_income_upper = average_income[1]
    

#Query the data based on the users selection parameters
    df_selection = df.query('''
    Status == @status \
    & Number_of_Properties == @num_props \
    & Council == @council \
    & Consent == @consent \
    & Minor_Variance == @minor_variance \
    & Official_Plan_Rezoning == @official_plan \
    & Site_Plan_Application == @site_plan \
    & Average_Income >= @average_income_lower \
    & Average_Income <= @average_income_upper\
    ''')

    st.subheader(f"**There are {len(df_selection)} applications that meet these parameters.**")
    st.map(df_selection)