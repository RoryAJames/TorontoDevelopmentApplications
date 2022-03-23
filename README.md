[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/roryajames/torontodevelopmentapplications/main/app.py)

# Toronto Development Applications

This repository is still a work in progress!

## Project Overview

An application that allows users to find out where development applications in the City of Toronto have been approved, and where they have been denied. This app provides users with the ability to filter and view development application data based on a range of geospatial parameters, such as application type, number of properties, zoning category, average neighourhood income, and more! Users can also predict the likelihood that an application will receive an approval based on parameters that the user provides. [Check out there app here!](https://share.streamlit.io/roryajames/torontodevelopmentapplications/main/app.py) 

## The Inspiration and Business Case

The inspiration for this project came to me from two places:

1) I wanted to provide an easier way for planners and real estate professionals in Toronto to view development application data. The current way to view this data is through the [City of Toronto Application Information Centre](https://www.toronto.ca/city-government/planning-development/application-information-centre/). While this portal does provide a good service, it doesn't give the user the ability to filter and view the data based on geospatial parameters that the user might be interested in.    
   
2) I know that it is very costly when a development application is denied. In these situations, the developer is left to either go back to the drawing board, or appeal the decision. While the review and outcome of each application is supposed to be independent, I suspected that the outcome of an application could be predicted based on the details of the application itself. With this in mind, I wanted to build a tool that could help developers during their due diligence phase by providing them with an estimated likelihood that their application will receive an approval. 

## The Data

Data for this project was obtained from the [City of Toronto Open Data Portal](https://open.toronto.ca/). Here is a complete list of all the data sources that I gathered:

- [Development Applications](https://open.toronto.ca/dataset/development-applications/)
- [Community Council Boundaries](https://open.toronto.ca/dataset/community-council-boundaries/)
- [Boundaries of the City of Toronto neighbourhoods](https://open.toronto.ca/dataset/neighbourhoods/) and [ their respective 2016 profiles](https://open.toronto.ca/dataset/neighbourhood-profiles/).
- [Secondary Plan Areas](https://open.toronto.ca/dataset/secondary-plans/)
- [Business Improvement Areas](https://open.toronto.ca/dataset/business-improvement-areas/)
- [Site and Area Specific Policies](https://open.toronto.ca/dataset/site-and-area-specific-policies/)
- [Zoning Bylaw No. 569-2013](https://open.toronto.ca/dataset/zoning-by-law/)
  
## A Few Notes

- I arbitrarily decided to subset the development application data and build the app using development applications that have been applied for on or after May 3rd 2017. I chose this date because it was the day that the Toronto Local Appeal Body (TLAB) came into effect.
  
- My definition of denied applications include the applications that are currently under appeal, or have received an approval following an appeal. The reason for this is that the application was initially denied. I know that it is common for applications to be appealed because a decision was delivered in the alloted review time set out in the Planning Act. However, based on the way the city stores their data, I cannot determine whether this is the case. I decided it would be best to proceed on the assumption that all applications were formally denied.
  
- While the prediction abilities of this app are respectable, I know that far more data points are required to justify the apps use in a business setting. In its current state the app is missing the important granular details of the development applications. These are details like the proposed land use, the planning rationale, lot details, unit breakdown, floor space ratio, architectural plans, etc. While these details are made publicly available on the Application Information Centre, they are not easily accessible at scale. While I would like to build a full fledged app that has these details, it would be a massive undertaking and require the work of several data engineers.

## Model Performance

A Logistic Regression and Random Forest model were used to predict the outcome of applications. Precision was the preferred evaluation metric to compare the performance of the two models, since it is far more costly to have false positives in this particular business context. An example of a false positive here would be a case where the predicted outcome of an application is approved but in actuality it was denied. 

The Random Forest model outperformed the logistic on a precision basis, and was therefore used as the model to predict the estimated approval likelihood of an application. Here is a breakdown of some of the other performance metrics that were evaluated:

| Model                 | Accuracy       | Precision   | Recall    | ROC AUC |
| -------------         |:-------------: | :-----:     | :-----:   | :-----: |
| Logistic Regression   | 69%            |  69%        | 92%       | 60%     |
| Random Forest         | 71%            |  72%        | 89%       | 64%     |

## Data Wrangling

Here is an overview of the major data wrangling steps I performed:

- Applications were placed into a binary category (either approved or denied) based on the key words found in City of Toronto development applications dataset.
  
- Part lot, condominium, subdivision, and TLAB applications were removed from the analysis either due to low frequencies or variance. TLAB applications were removed for the sake of reducing duplicates.
  
- Since multiple properties can belong to one application, the application reference numbers were grouped together, which generated the total number of properties for each application. The number of properties were later binary encoded to distinguish applications that represent one or more properties.
  
- It is pretty common for applications to have multiple application types. For example, an official plan and site plan application can be submitted at the same time. The same is true for minor variance and consent applications. In order to capture this, each applications address and application type were grouped together and binary encoded.
   
- Latitude and longitude were extracted from each application by geocoding the applications address using Nominatim. Once latitude and longitude were extracted, I was able to perform spatial joins for each application and pair it with the city spatial data.
## Exploratory Data Analysis - Key Findings

Two types of statistical tests were performed to determine the features that should be included in the prediction model. Chi-square tests were performed on each of the categorical features, while a logistic regression model with a backward selection method was fit on all of the numerical features.

These tests showed that the following features were statistically significant, and thus made for good predictors in classifying an applications status:

- The number of properties (one property vs more than one property).
  
- Consent, minor variance, official plan rezoning, and site plan application types.
  
- The council that an application is located in.
  
- Whether the application is located in a secondary plan area.
  
- The average income of the neighbourhood that the application is located in.

I will note the following:

- Neighbourhoods were found to be statistically significant in predicting an applications status. However there were 133 neighbourhoods observed in the dataset. Including this as a feature would have greatly increased the models complexity and dimensionality. Since neighbourhoods can be consolidated down to just four councils, I opted to not include it as a feature in the prediction model.
  
- The zoning category was not found to be statistically significant in predicting an applications status. However, I suspect this was due to a large imbalance of zoning categories.
