# Toronto Development Applications

This repository is still a work in progress!

## Project Overview

This project will explore development applications in the City of Toronto and compare applications based on their development status.

## The Inspiration and Business Case

It can be very costly for developers to have a development application denied. If an application is denied the developer is left to either go back to the drawing board, or appeal the decision.

While the review and outcome of each application is independent, and not supposed to be impacted by precedent, I wanted to know whether the outcome of an application can be predicted based on the parameters of the application itself.

## The Data

Data for this project was collected from the [City of Toronto Open Data Portal](https://open.toronto.ca/). Here is a complete list of all the data sources that I gathered:

- [Development Applications](https://open.toronto.ca/dataset/development-applications/)
- [Community Council Boundaries](https://open.toronto.ca/dataset/community-council-boundaries/)
- [Boundaries of the City of Toronto neighbourhoods](https://open.toronto.ca/dataset/neighbourhoods/) and [ their respective 2016 profiles](https://open.toronto.ca/dataset/neighbourhood-profiles/).
- [Secondary Plan Areas](https://open.toronto.ca/dataset/secondary-plans/)
- [Business Improvement Areas](https://open.toronto.ca/dataset/business-improvement-areas/)
- [Site and Area Specific Policies](https://open.toronto.ca/dataset/site-and-area-specific-policies/)
- [Zoning Bylaw No. 569-2013](https://open.toronto.ca/dataset/zoning-by-law/)

## A Few Notes

- I arbitrarily decided to only look at applications that have been applied for on or after May 3rd 2017. I chose this date because it was the day that the Toronto Local Appeal Body (TLAB) came into effect.
  
- My definition of denied applications include those that are currently under appeal, or have received an approval following an appeal. The reason for this is that the application was initially denied, and therefore should be labeled as such. I know it is common for applications to be appealed because the city failed to make a decision on the application in the alloted review time set out by the Planning Act. However, based on the way the data is presented I cannot determine whether this is the case at scale.

## Data Wrangling

Here is an overview of the major data wrangling steps I performed:

- Applications were placed into a binary category (approved or denied) based on the key words found in City of Toronto development application dataset.
  
- Part lot, condominium, subdivision, and TLAB applications were removed from the analysis. Part lot applications were removed since these applications take place after construction. Condominium applications were removed since all of the observed applications were approved. Subdivision applications were removed because there were only 14 observations. TLAB applications were removed since these applications are mere duplicates of applications that have already been made and subsequently denied.
  
- Application numbers were combined in order to generate the number of properties that an application has. The number of properties were later binary encoded into applications that are either one property or more than one property.
  
- Application types were binary encoded based on the applications address. This was done in order to group applications together and eliminate duplicates. It is pretty common for applications to have more than one application type. For example, an official plan and site plan application can be submitted at the same time. The same for minor variance and consent applications
   
- Latitude and longitude were extracted from each application by geocoding the applications address using Nominatim.

## Exploratory Data Analysis - Key Findings

Two types of statistical tests were conducted to determine which features should be included in predicting an applications status. Chi-square tests were performed on each of the categorical features, while a logistic regression model was fit on all of the numerical features.

These tests showed that the following features were statistically significant, and thus made for good predictors in classifying an applications status:

- The number of properties (one property vs more than one property).
  
- Consent, minor variance, official plan rezoning, and site plan application types.
  
- The council that an application is located in.
  
- Whether the application is located in a secondary plan area.
  
- Whether the application is located in a site or area that has a specific policy.
  
- The number of households deemed to be in core housing need in the neighbourhood that the application is located in.

I will note that neighbourhoods were found to be statistically significant in predicting an applications status. However there are 132 neighbourhoods in Toronto. Including this as a feature would greatly increase the models complexity and dimensionality. Since neighbourhoods can be consolidated down to councils, I opted for not including it as a feature in the prediction model.

## Lessons That I Learned
