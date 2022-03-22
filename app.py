import streamlit as st
from streamlit_option_menu import option_menu
from apps.about import show_about_page
from apps.explore_page import show_explore_page, page_load
from apps.predict_page import show_predict_page

page_load()

with st.sidebar:
    selected = option_menu("Main Menu",
                           options = ("About", "Explore", "Predict"),
                           icons=("house","search","bullseye"),
                           menu_icon="cast")

if selected == "About":
    show_about_page()

elif selected == "Explore":
    show_explore_page()
    
else:
    show_predict_page()
    
st.sidebar.info(
        """
        This app was built by Rory James
        
        Data for this project was sourced from the [City of Toronto Open Data Portal](https://open.toronto.ca/)
        
        [Click Here For The Project Source Code](https://github.com/RoryAJames/TorontoDevelopmentApplications) 
        
        Feel free to connect with me:        
        [GitHub](https://github.com/RoryAJames) | [LinkedIn](https://www.linkedin.com/in/rory-james-873493111/)
        
    """
    )