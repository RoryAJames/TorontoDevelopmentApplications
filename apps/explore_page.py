from email.mime import application
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

    st.title('Explore Development Applications in the City of Toronto')

##Row 1
    row1_col1, row1_col2, row1_col3 = st.columns([0.6, 1, 2])

    with row1_col1:
        status = st.selectbox("Status", df.Status.unique())

    with row1_col2:
        num_props = st.selectbox("Number of Properties", df.Number_of_Properties.unique())
    
    with row1_col3:
        council = st.multiselect("Council", df.Council.unique())

 ## Row 2   

    row2_col1, row2_col2 = st.columns([1, 2])

    with row2_col1:
        application_type = st.multiselect("Application Type", ('Consent','Minor Variance',
        'Official Plan Rezoning', 'Site Plan Application'))

    
    if 'Consent' in application_type:
        consent = 1
    else:
        consent = 0
    
    if 'Minor Variance' in application_type:
        minor_variance = 1
    else:
        minor_variance = 0

        
    ##### Need to update the names of official plan and site plan with _
    
    
    with row2_col2:
        house_in_need = st.slider("Number of Households In Core Housing Need",value=(100,6000))
        house_in_need_lower = house_in_need[0]
        house_in_need_upper = house_in_need[1]
    

#Query the data based on the user parameters
    df_selection = df.query('''
    Status == @status \
    & Number_of_Properties == @num_props \
    & Council == @council \
    & Consent == @consent \
    & Minor_Variance == @minor_variance \
    & Households_In_Core_Housing_Need >= @house_in_need_lower \
    & Households_In_Core_Housing_Need <= @house_in_need_upper\
    ''')

    st.write(f"There are {len(df_selection)} applications that meet these parameters.")
    st.map(df_selection)
    st.write(df_selection)