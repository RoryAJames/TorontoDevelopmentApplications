# Toronto Development Applications

This repository is still a work in progress!

## Project Overview

This project will explore development applications in the City of Toronto and compare applications based on their development status.

## The Inspiration and Business Case

It can be very costly for developers to have a development application denied. If an application is denied the developer is left to either go back to the drawing board, or appeal the decision. 

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
  
- My definition of denied applications include those that are currently under appeal, or received an approval following an appeal. The reason for this is that the application was initially denied by council, and therefore should be labeled as such. I know it is common for applications to be appealed because the city failed to make a decision on the application in the alloted review time set out by the Planning Act. However, based on the way the data is presented I cannot determine whether this is happening.
  

## Data Wrangling

Here is an overview of the major data wrangling steps I performed:

- Applications were placed into a binary category (approved or denied) based on key words in City of Toronto development application status.
  
- Part lot, condominium, subdivision, and TLAB applications were removed from the analysis.
  
- Application numbers were combined in order to generate the number of properties that were effected by each application. The number of properties were later binary encoded into applications with one property, and those with more than one property.
  
- Application types were binary encoded based on the applications address. This was done in order to group applications together, while also eliminating duplicate applications. It is pretty common for applications to have more than one application type. For example, an official plan and site plan application can be submitted at the same time. The same can apply to minor variance and consent applications
   
- Latitude and longitude were extracted from each application by geocoding the applications address using Nominatim.

## Exploratory Data Analysis - Key Findings

Two types of statistical tests were performed to determine whether features would make for good predictors in determining an applications approval. Chi-square tests were performed on each of the categorical features, while a logistic regression model was fit on all of the numerical features.

## Lessons That I Learned
