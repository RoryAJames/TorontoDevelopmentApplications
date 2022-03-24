import streamlit as st

def show_about_page():
    
    st.title('Development Applications In The City of Toronto')
    
    st.write("""This is a proof of concept application that is designed to help Urban Planners and Real Estate professionals in the City of Toronto. This app providers users with
             an easy way to filter and view development application data based on geospatial parameters. In addition, this app gives users the ability to predict the estimated likelihood that 
             an application will receive an approval.""")
    
    st.subheader("Explore Applications Based On Approval Status")
    
    st.write("""Find out where applications have been approved, and where they have been denied. Filter applications based on a range of geospatial datapoints such as application type,
             number of properties, zoning category, average neighourhood income, and more!""")
    
    with st.expander("Click Here To See A Demo."):
        st.image("images/explorepage.gif")
    
    st.subheader("Predict the Likelihood than an Application Receives Approval")
    
    st.write("Use Machine Learning to predict the outcome of an application! Enter an applications parameters and get an estmated likelihood that the application will receive approval.")
    
    with st.expander("Click Here To See A Demo."):
        st.image("images/predictpage.gif")