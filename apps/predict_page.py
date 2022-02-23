import streamlit as st
import pandas as pd
import numpy as np
import pickle


@st.cache(allow_output_mutation=True)
def load_model():
    with open('prediction_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

classifier = data["model"]
scaler = data["income_scaler"]

def show_predict_page():
    
    st.title('Predict The Likeliehood An Application Receives Initial Approval')
    
    num_props = st.selectbox("How Many Properties Are On The Application", ('One','More Than One'))
    
    council = st.selectbox("What Council Is The Application Located In", ('Etobicoke York Community Council','North York Community Council','Scarborough Community Council', 'Toronto and East York Community Council'))
    
    application_type = st.multiselect("What Is The Application Type", ('Consent','Minor Variance','Official Plan Rezoning', 'Site Plan Application'))
    
    secondary_pan = st.selectbox("Is The Application In A Secondary Plan Area", ('Yes','No'))
    
    average_income = st.number_input("What Is The Average Income In The Neighbourhood The Application Is Located In", value= 50000)
    
    ok = st.button("Predict Initial Approval Likelihood")
    
    if ok:
        X = np.array([[num_props, consent, minor_var, official_plan, site_plan, secondary_plan, avgincome, etobicoke, north_york, scarb, to_ey]])
        X[:, 6] = scaler.transform((X[:,6]).reshape(-1,1)) #Scale the user input
        X.astype(float) #Us float since data is being scaled
        
        final_pred = classifier.predict_proba(X)
        st.subheader(f"There is a {final_pred[0][1]:.2%} chance this application receives an initial approval.") #Print prediction result to screen