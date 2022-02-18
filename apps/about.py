import streamlit as st

def show_about_page():
    
    st.title('Development Applications In The City of Toronto')
    st.markdown("""Welcome to the City of Toronto Development Application Portal! This is a proof of concept application that is intended to give users the ability
                to view development applications in the City of Toronto. based on their application status - either approved or denied. In addition, this app allows users to predict the likelihood that an application will receive approval based on the applications perameters.
                All of the data for this project was sourced from 
                the [City of Toronto Open Data Portal](https://open.toronto.ca/). The source code for this app can be found [here](https://github.com/RoryAJames/TorontoDevelopmentApplications).
    """)