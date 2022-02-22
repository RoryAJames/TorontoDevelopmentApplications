import streamlit as st
import pandas as pd
import pickle


@st.cache
def get_data():
    df = pd.read_excel('data\combined_files_output.xlsx')
    return df

df = get_data()

def show_predict_page():
    
    st.title('Predict The Likeliehood An Application Is Approved')
    
    num_props = st.selectbox("How Many Properties Are On The Application", ('One','More Than One'))
    
    council = st.selectbox("What Council Is The Application Located In", df.Council.unique())
    
    application_type = st.multiselect("What Is The Application Type", ('Consent','Minor Variance','Official Plan Rezoning', 'Site Plan Application'))
    
    secondary_pan = st.selectbox("Is The Application In A Secondary Plan Area", ('Yes','No'))
    
    average_income = st.number_input("What Is The Average Income In The Neighbourhood The Application Is Located In", value= 50000)
    
    ok = st.button("Predict Approval Likelihood")
    
    st.subheader("The estimated likeliehood that this application is approved is _%")