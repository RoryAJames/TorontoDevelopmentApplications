import streamlit as st

def show_about_page():
    
    st.title('Development Applications in the City of Toronto')
    st.markdown("""This interactive dashboard is designed for visualizing development applications in the City of Toronto. Specifically, the intent of the dashboard is to give users the
    functionality to visualize applications based on their decision status, and the various parameters of the applications. All of the data for this project was sourced from
    the [City of Toronto Open Data Portal](https://open.toronto.ca/).
    """)