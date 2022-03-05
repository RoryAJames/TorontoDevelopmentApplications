import streamlit as st

def show_about_page():
    
    st.title('Development Applications In The City of Toronto')
    
    st.write("""This is a proof of concept application that is designed to help the Planners and Real Estate professionals in Toronto explore and predict the outcome of
             development applications in the City of Toronto.""")
    
    st.subheader("An Easier Way To View The Applications You Are Interested In")
    
    st.write("""Search and filter applications based on your interests. 
             such as application type, approval status, number of properties, zoning category, average neighbourhood income, and more!""")
    
    with st.expander("Click Here To See A Demo."):
        st.image("https://i.imgur.com/Z3dk6Tr.gif")
    
    st.subheader("Predict The Likelihood That Your Application Receives Approval")
    
    st.write("Enter the parameters of your application and get the estimated likeliehood that your application will be approved.")
    
    with st.expander("Click Here To See A Demo."):
        st.image("https://i.imgur.com/Z3dk6Tr.gif")