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
    
    st.title('Predict the Likelihood than an Application Receives Approval')
    
    ## NUMBER OF PROPERTIES
    
    num_props = st.selectbox("How Many Properties Are On The Application", ('One','More Than One'))
    
    if num_props == 'One':
        num_props = 1
    else:
        num_props = 0
    
    ## COUNCIL
    
    council = st.selectbox("What Council Is The Application Located In", ('Etobicoke York Community Council','North York Community Council','Scarborough Community Council',
                                                                          'Toronto and East York Community Council'))
    
    if council == 'Etobicoke York Community Council':
        etobicoke = 1
        
    else:
        etobicoke = 0
    
    if council == 'North York Community Council':
        north_york = 1
        
    else:
        north_york = 0
        
    if council == 'Scarborough Community Council':
        scarb = 1
        
    else:
        scarb = 0
    
    if council == 'Toronto and East York Community Council':
        to_ey = 1
        
    else:
        to_ey = 0
        
     ## APPLICATION TYPE
    
    application_type = st.multiselect("What Is The Application Type", ('Consent','Minor Variance','Official Plan Rezoning', 'Site Plan Application'))
    
    if 'Consent' in application_type:
        consent = 1
    else:
        consent = 0
    
    if 'Minor Variance' in application_type:
        minor_var = 1
    else:
        minor_var = 0

    if 'Official Plan Rezoning' in application_type:
        official_plan = 1
    else:
        official_plan = 0
    
    if 'Site Plan Application' in application_type:
        site_plan = 1
    else:
        site_plan = 0
    
    ## SECONDARY PLAN
    
    secondary_plan = st.selectbox("Is The Application Located In A Secondary Plan Area", ('No','Yes'))
    
    if secondary_plan == 'Yes':
        secondary_plan = 1
    
    else:
        secondary_plan = 0
        
    ## AVERAGE INCOME
    
    average_income = st.number_input("What Is The Average Income In The Neighbourhood The Application Is Located In", value= 0)
    
    ok = st.button("Predict Approval Likelihood")
    
    #Execute if button is clicked
    
    if ok:
        X = np.array([[num_props, consent, minor_var, official_plan, site_plan, secondary_plan, average_income, etobicoke, north_york, scarb, to_ey]])
        X[:, 6] = scaler.transform((X[:,6]).reshape(-1,1)) #Scale the user input
        X.astype(float) #Use float since average income is being scaled
    
        final_pred = classifier.predict_proba(X)
        st.subheader(f"There is an estimated {final_pred[0][1]:.0%} chance that this application will be approved.") #Print prediction result to screen