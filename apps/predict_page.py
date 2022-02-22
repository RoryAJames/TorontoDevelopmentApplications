import streamlit as st
import pandas as pd

@st.cache
def get_data():
    df = pd.read_excel('data\combined_files_output.xlsx')
    return df

df = get_data()

def show_predict_page():
    
    st.title('Predict An Applications Approval Status')
    st.markdown('Please select the application perameters you are interested in predicting!')
    status = st.selectbox("Select The Application Status", df.Zoning_Category.unique())