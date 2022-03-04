import streamlit as st

def show_about_page():
    
    st.title('Development Applications In The City of Toronto')
    
    st.write("""This is a proof of concept application that is designed to help Planners and Real Estate professionals explore and predict the outcome of
             development applications in the City of Toronto.""")
    
    st.subheader("An Easier Way To Filter And View Applications")
    
    st.write("View applications based on your interests. Filter down such as application type, approval status, number of properties, zoning category, average neighbourhood income, and more!")
    
    with st.expander("Click here to see a demo."):
        st.image("https://i.imgur.com/Z3dk6Tr.gif")
    
    st.subheader("Predict The Likelihood Your Application Receives Approval")
    
    st.write("Enter the parameters of your application and get the estimated likeliehood that your application will be approved.")
    
    with st.expander("Click here to see a demo."):
        st.image("https://i.imgur.com/Z3dk6Tr.gif")