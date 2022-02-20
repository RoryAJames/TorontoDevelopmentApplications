import streamlit as st
from apps.about import show_about_page
from apps.explore_page import show_explore_page
from apps.predict_page import show_predict_page


page = st.sidebar.radio("Selection Menu", ("About", "Explore", "Predict"))

if page == "About":
    show_about_page()
elif page == "Explore":
    show_explore_page()
else:
    show_predict_page()