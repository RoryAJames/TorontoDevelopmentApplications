import streamlit as st

def show_predict_page():
    
    st.title('Predict Whether An Application Will Be Approved or Denied')
    st.markdown("""Please select the paramters of an application that you would like to predict.
                Please note that the following option parameters were found to be statistically significant in predicting
                the outcome of an application through exploratory data analysis. 
    """)