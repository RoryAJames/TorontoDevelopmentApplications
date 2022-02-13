# Toronto Development Applications

This repository is still a work in progress!

## Project Overview

This project will explore development applications in the City of Toronto and compare applications based on their development status.

## The Inspiration and Business Case

It can be very costly for developers to have a development application denied. If an application is denied the developer is left to either go back to the drawing board, or appeal the decision. 

## The Data

Data for this project was collected from the [City of Toronto Open Data Portal](https://open.toronto.ca/). Here is a complete list of all the data sources I gathered and combined:

- [Development Applications](https://open.toronto.ca/dataset/development-applications/)
- [Community Council Boundaries](https://open.toronto.ca/dataset/community-council-boundaries/)
- [Boundaries of the City of Toronto neighbourhoods](https://open.toronto.ca/dataset/neighbourhoods/) and [ their respective 2016 profiles](https://open.toronto.ca/dataset/neighbourhood-profiles/).
- [Secondary Plan Areas](https://open.toronto.ca/dataset/secondary-plans/)
- [Business Improvement Areas](https://open.toronto.ca/dataset/business-improvement-areas/)
- [Site and Area Specific Policies](https://open.toronto.ca/dataset/site-and-area-specific-policies/)
- [Zoning Bylaw No. 569-2013](https://open.toronto.ca/dataset/zoning-by-law/)

## A Few Notes

- I arbitrarily decided to only look at applications that have been applied for on or after May 3rd 2017. I chose this date because it was the day that the Toronto Local Appeal Body (TLAB) came into effect.
  
- My definition of denied applications include those that are currently under appeal, or received an approval following an appeal. The reason for this is that the application was initially denied by council, and therefore should be labeled as such. I know there are applications that are appealed because a decision was not made in the alloted application review time set forth by the Planning Act. However, based on the way the data is presented I have no idea 

## Data Wrangling

Here is an overview of the major data wrangling steps I performed:

- Applications were placed into a binary category based on the application status - either approved or denied.
  
- Part lot and TLAB applications were removed.
   
- Geocoded applications based on their address using Nominatim. 
   
- 

## Exploratory Data Analysis - Key Findings

## Lessons That I Learned
