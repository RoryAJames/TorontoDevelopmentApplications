import streamlit as st


def show_about_page():
    
    st.title('Development Applications In The City of Toronto')
    
    st.markdown("""This is a proof of concept application that is designed to help Toronto planners and real estate professionals. First, it allows users to view development applications in the City of Toronto 
                based on application approval status, along with a range of other paramters. Second, it gives users the option to predict the likelihood that an application will receive approval based on the applications features.  \n"""
    )