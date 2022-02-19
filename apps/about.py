import streamlit as st

def show_about_page():
    
    st.title('Development Applications In The City of Toronto')
    st.markdown("""This is a proof of concept application that allows users to filter and view development applications in the City of Toronto based on desired parameters.  
                Click here to see a demo of how it works!
                In addition, this app allows users to predict the likelihood that an application will receive approval based on the applications perameters. 
                Click here to see a demo of how it works!
                All of the data for this project was sourced from 
                the [City of Toronto Open Data Portal](https://open.toronto.ca/). The source code for this app can be found [here](https://github.com/RoryAJames/TorontoDevelopmentApplications).
    """)