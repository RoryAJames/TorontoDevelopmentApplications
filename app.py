import streamlit as st
from apps.about import show_about_page
from apps.explore_page import show_explore_page
from apps.predict_page import show_predict_page

page = st.sidebar.radio("Select", ("About", "Explore", "Predict"))

if page == "About":
    show_about_page()
elif page == "Explore":
    show_explore_page()
else:
    show_predict_page()

st.sidebar.info(
        """
        This app was built and maintained by Rory James.
        
        All of the data for this project was sourced from the [City of Toronto Open Data Portal](https://open.toronto.ca/) 
        
        Feel free to connect with me:        
        [GitHub](https://github.com/RoryAJames) | [LinkedIn](https://www.linkedin.com/in/rory-james-873493111/)
        
        [Click Here For Project Source Code](https://github.com/RoryAJames/TorontoDevelopmentApplications)
    """
    )