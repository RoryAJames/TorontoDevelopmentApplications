import streamlit as st

def show_about_page():
    
    st.title('Development Applications In The City of Toronto')
    
    st.write("""This is a proof of concept application that is designed to help Urban Planners and Real Estate professionals in the City of Toronto, by providing
             them with an easier way to view development application data. In addition, this tool gives users the ability to predict the estimated likelihood that 
             an application will receive an approval based on it's parameters.""")
    
    st.subheader("Explore Applications Based On Approval Status")
    
    st.write("""An easier way to see where development applications have been either approved or denied. 
             Search and filter applications based on a range of geospatial datapoints such as application type, number of properties, zoning category, average neighourhood income,
             and more!""")
    
    with st.expander("Click Here To See A Demo."):
        st.image("images\explorepage.gif")
    
    st.subheader("Predict The Likelihood That Your Application Receives Approval")
    
    st.write("Use Machine Learning to predict the estimated likeliehood that an application will be approved!")
    
    with st.expander("Click Here To See A Demo."):
        st.image("images\predictpage.gif")