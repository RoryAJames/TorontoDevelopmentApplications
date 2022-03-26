import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(layout="wide")

@st.cache
def get_data():
    df = pd.read_csv('data/explore_page_data.csv')
    return df

df = get_data()

def show_explore_page():
    
    st.title('Explore Development Applications In The City of Toronto')

##Row 1
    row1_col1, row1_col2, row1_col3 = st.columns([1, 1, 1])

    with row1_col1:
        status = st.selectbox("Select The Application Status", df.Status.unique())

    with row1_col2:
        num_props = st.multiselect("Select The Number of Properties", df.Number_of_Properties.unique())
    
    with row1_col3:
        council = st.multiselect("Select The Council(s) Of Interest", df.Council.unique())

 ## Row 2   

    row2_col1, row2_col2, row2_col3 = st.columns([1, 1, 1])

    with row2_col1:
        application_type = st.multiselect("Select The Application Type(s)", ('Consent','Minor Variance',
        'Official Plan Rezoning', 'Site Plan Application'))

    #Check what has been selected from application type
    
    if 'Consent' in application_type:
        consent = 1
    else:
        consent = 0
    
    if 'Minor Variance' in application_type:
        minor_variance = 1
    else:
        minor_variance = 0

    if 'Official Plan Rezoning' in application_type:
        official_plan = 1
    else:
        official_plan = 0
    
    if 'Site Plan Application' in application_type:
        site_plan = 1
    else:
        site_plan = 0
        
    with row2_col2:
        zoning = st.multiselect("Select The Zoning Categories", (df.Zoning_Category.unique()))
            
    with row2_col3:
        policies = st.multiselect("Select Additional Policies", ('Secondary Plan Areas','Business Improvement Areas',
        'Site Specific Policy Areas'))
        
    if 'Secondary Plan Areas' in policies:
        secondary_plan = 1
        
    else:
        secondary_plan = 0
    
    if 'Business Improvement Areas' in policies:
        bia = 1
    else:
        bia = 0

    if 'Site Specific Policy Areas' in policies:
        site_specific = 1
    else:
        site_specific = 0
    
    #Row 3        
        
    average_income = st.slider("Select The Average Neighbourhood Income Range",value=(0,350000))
    average_income_lower = average_income[0]
    average_income_upper = average_income[1]
    

#Query the data based on the users selection
    df_selection = df.query('''
    Status == @status \
    & Number_of_Properties == @num_props \
    & Council == @council \
    & Consent == @consent \
    & Minor_Variance == @minor_variance \
    & Official_Plan_Rezoning == @official_plan \
    & Site_Plan_Application == @site_plan \
    & Zoning_Category == @zoning \
    & Secondary_Plan == @secondary_plan \
    & Business_Improvement_Area == @bia \
    & Site_and_Area_Specific_Policy == @site_specific \
    & Average_Income >= @average_income_lower \
    & Average_Income <= @average_income_upper\
    ''')
    
    #Display how many applications meet the query parameters

    if len(df_selection) == 0:
        st.subheader("There are no applications that meet these parameters.")
    elif len(df_selection) == 1:
        st.subheader("Only one application meets these parameters.")
    else:
        st.subheader(f"There are {len(df_selection)} applications that meet these parameters.")
    
    # Pass the query to a pydeck scatterplot
    
    scatter_layer = pdk.Layer(
        "ScatterplotLayer",
        data = df_selection,
        pickable=True,
        get_position='[lon, lat]',
        get_color='[200, 30, 0, 160]',
        get_radius=200,
    )
    
    text_layer = pdk.Layer(
        'TextLayer',
        data=df_selection,
        pickable=False,
        get_position='[lon, lat]',
        getTextAnchor= '"middle"',
        get_alignment_baseline='"bottom"')
    
    layers = [scatter_layer,text_layer]
    
    view_state = pdk.ViewState(latitude=df['lat'].mean(), longitude=df['lon'].mean(), zoom=10)
    
    r = pdk.Deck(layers=[layers], map_style='mapbox://styles/mapbox/light-v9',
                 initial_view_state=view_state, tooltip={"text": "<b>Council: </b> {council} <br /> "
                                                                 "<b>Number of Properties: </b> {num_props} <br /> "
                                                                 })
    
    st.pydeck_chart(r)
    
    """ 
    
    tooltip = {
             "html":
                 "<b>Number of Properties:</b> {num_props} <br/>"
                 "<b>Council:</b> {council} <br/>",
                 "style": {"color": "black"}
                 }

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        
        #Set the initial view to coordinates of Toronto
        initial_view_state=pdk.ViewState(
            latitude= 43.6532,
            longitude=-79.3832,
            zoom=10),
        
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df_selection,
                pickable=True,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200),
            
            pdk.Layer(
                'TextLayer',
                data=df_selection,
                pickable=False,
                get_position='[lon, lat]',
                get_text=["name"],
                getTextAnchor= '"middle"',
                get_alignment_baseline='"bottom"')
            ],
        tooltip= tooltip
        )
        ) """