import streamlit as st


def show_about_page():
    
    st.title('Development Applications In The City of Toronto')
    
    st.markdown("""This is a proof of concept application that is designed to help Toronto planners and real estate professionals.
                With this app, users can view development applications in the City of Toronto based on application approval status, along with a range of other paramters.
                Users can also predict the likelihood that an application will receive approval based on the applications features."""
    )
    
    with st.expander("Click Here To See A Demo"):
        st.write("To be a GIF")
        
    st.info("Click on the left sidebar menu to navigate to the different apps.")