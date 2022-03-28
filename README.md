[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/roryajames/torontodevelopmentapplications/main/app.py)
## Project Overview

A Streamlit application that allows users to find out where development applications in the City of Toronto have been approved, and where they have been denied. This app provides users with the ability to filter and view development application data based on geospatial parameters, such as application type, number of properties, zoning category, average neighourhood income, and more! Users can also predict the likelihood that an application will receive approval based on application details that the user provides. [Check out there app here!](https://share.streamlit.io/roryajames/torontodevelopmentapplications/main/app.py) 

## The Inspiration and Business Case

The inspiration for this project came to me from two places:

1) I wanted to provide an easier way for Urban Planners and Real Estate professionals in Toronto to view development application data. The current way to view this data is through the [City of Toronto Application Information Centre](https://www.toronto.ca/city-government/planning-development/application-information-centre/). While this portal does provide a good service, it doesn't offer the ability to filter and view the data based on parameters that the user might be interested in.    
   
2) I know that it can be very costly when a development application is denied by the city. In these situations, the developer is left to either go back to the drawing board, or appeal the decision. While the review and outcome of each application is supposed to be independent, I believe that the outcome of an application can be predicted based on the details of the application itself. As such, I wanted to build a tool that helps developers with their due diligence, and allow them to calculate an estimated likelihood that their application will be approved. 

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

- I arbitrarily decided to subset the data and build this app using development applications that have been applied for on or after May 3rd 2017. I chose this date because it was the day that the Toronto Local Appeal Body (TLAB) came into effect.
  
- My definition of a "denied application" includes the applications that are currently under appeal, or have received an approval following an appeal. The reason for this is that the application was initially denied. I know that it is common for applications to be appealed because the city did not deliver a decision in the alloted review time set out in the Planning Act. However, given the way the city presents the data, I cannot determine whether this is the case. I decided it would be best to proceed on the assumption that all appealed applications were formally denied based on the merits of the application.
  
- While I am happy with the prediction abilities of this application, I know that far more data points are required to justify its use in a business setting. In its current state, the app is missing the important granular details of development applications. These are details like the proposed land use, the planning rationale, lot details, unit breakdown, floor space ratio, architectural plans, etc. While these details are publicly available on the Application Information Centre, they are not easily accessible at scale. While I would like to build a full fledged app that takes these details into consideration, it would be a massive undertaking and require the work of several data engineers to scrape and store the data. Given that this app is just a proof of concept, I opted to only use features that were found to be statistically significant in my exploratory data analysis. 

## Model Performance

Predicting the estimated likelihood that an application is approved is a binary classification problem.

A Logistic Regression and Random Forest model were first used to predict the outcome of applications - either approved or denied. Precision was the preferred evaluation metric to compare the performance of the two models, since it is far more costly to have false positives in this particular business context. An example of a false positive here would be a case where the predicted outcome of an application is approved, but in actuality it is denied.

Due to imbalances observed in the dataset, I opted to use a stratified five fold cross validation grid search to train the models. 

Random Forest outperformed the logistic regression on a precision basis, and was thus used as the model in the application. Since the overall goal of the app was to predict the estimated likelihood that an application is approved, the model outputs the probability that an application belongs to the approved class. Here is a breakdown of some of the other performance metrics that were evaluated:

| Model                 | Accuracy       | Precision   | Recall    | ROC AUC |
| -------------         |:-------------: | :-----:     | :-----:   | :-----: |
| Logistic Regression   | 69%            |  69%        | 92%       | 60%     |
| Random Forest         | 71%            |  72%        | 89%       | 64%     |

## Data Wrangling

All of the data gathering and cleaning steps that I performed can be found in my [data wrangling](https://github.com/RoryAJames/TorontoDevelopmentApplications/blob/261d4fe571267feeb986f502c187f40e9700206c/notebooks/Toronto%20Development%20Application%20Data%20Wrangling%20and%20Geocoding.ipynb) and [combining files](https://github.com/RoryAJames/TorontoDevelopmentApplications/blob/be41b89d14d7a2ed3e1ef87ba657288496f3d977/notebooks/Combining%20Files.ipynb) notebooks. Here is a brief overview of some of the major tasks that I preformed:

- Applications were placed into a binary category (either approved or denied) based on key words found in City of Toronto development applications dataset.
  
- Part lot, condominium, subdivision, and TLAB applications were removed from the analysis due to low frequencies or variance. TLAB applications were removed for the purposes of reducing duplicates.
  
- Since multiple properties can belong to one application, the application reference numbers were grouped together, which generated the total number of properties for each application. It was found that an overwhelming majority of applications were for just one property. While this was originally intended to be a numerical feature, given its high degree of skew I opted to convert it into to a categorical feature (one property vs more than one property) and label encode it.
  
- It is pretty common for a property to have multiple applications submitted to the city concurrently. For example, an official plan and site plan application can be submitted together, even though the city presents the data as two separate applications. The same is true for minor variance and consent application types. In order to capture this, each applications address and application type were grouped together and dummy encoded.
   
- An applications latitude and longitude were extracted by geocoding the applications address. This step was preformed using Nominatim. Once latitude and longitude were extracted, I was able to perform spatial joins for each application and all of the geospatial datasets that I gathered. 
## Exploratory Data Analysis - Key Findings

Two types of statistical tests were conducted to determine the features that should be included in the prediction model. Chi-square tests were performed on each of the categorical features, while a logistic regression model with a backward selection method was fit on all of the numerical features.

These tests showed that the following features were statistically significant, and thus made for good predictors in classifying an applications outcome:

- The number of properties (one property vs more than one property).
  
- Consent, minor variance, official plan rezoning, and site plan application types.
  
- The council that an application is located in.
  
- Whether the application is located in a secondary plan area.
  
- The average income of the neighbourhood that the application is located in.

I will note the following:

- Neighbourhoods were found to be statistically significant in predicting an applications status. However, 133 neighbourhoods were observed in the dataset. Including this as a feature would have greatly increased the models complexity and dimensionality. Since neighbourhoods can be consolidated down to just four councils, I opted to not include it as a feature in the prediction model.

A complete breakdown of all the exploratory data analysis steps that I preformed [can be found in this notebook.](https://github.com/RoryAJames/TorontoDevelopmentApplications/blob/d5d1c4b41cf2224821769db4d845d8a6623e616b/notebooks/Exploratory%20Data%20Analysis.ipynb)
