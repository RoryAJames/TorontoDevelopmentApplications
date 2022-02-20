import streamlit as st

def show_about_page():
    
    st.title('Development Applications In The City of Toronto')
    
    st.markdown("""This is a proof of concept application that is designed to help planners and real estate professionals view development applications in the City of Toronto.
                Specifically, this tool gives users the functionality to filter and view applications based on approval status, along with a range of other paramters. 
                Click on Explore to see how it works!  \n"""
             
             "\n"
                
            "In addition, users can also predict the likelihood that an application will receive approval after specifying some key features. Click on Predict to see how it works!  \n"
            
            "\n"
                
            "All of the data for this project was sourced from the [City of Toronto Open Data Portal](https://open.toronto.ca/). A link to the project source code with additional details [can be found here](https://github.com/RoryAJames/TorontoDevelopmentApplications).  \n"
            
            "\n"
            
            "[Check out my Github page to see some of the other projects I have worked on!](https://github.com/RoryAJames) " 
    )