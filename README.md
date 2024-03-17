# Big-Mart-Sales-Prediction
A machine learning project to predict sales from a fictitious dataset.

**Overview**
Sales forecasting enables businesses to allocate resources for future growth while managing cash flow properly. Sales forecasting also assists firms in precisely estimating their expenditures and revenue, allowing them to predict their short- and long-term success. Retail Sales Forecasting also assists retailers in meeting customer expectations by better understanding consumer purchasing trends. This results in more
efficient use of shelf and display space within the retail establishment and optimal use of inventory space. The Bigmart sales forecast project can help you comprehend project creation in aprofessional atmosphere. This project entails extracting and processing data in SQL Server database using Azure Data Studio. before further processing and building various machine-learning models for sales prediction. The training file contains code to seamlessly integrate MY SQL Database into pandas. We will study several data processing techniques, exploratory data analysis, and
categorical correlation with Chi-squared, Cramer’s v tests, and ANOVA. In addition to basic statistical models like Linear Regression, we will learn how to design cutting-edgemachine-learning models like Gradient Boosting and Generalized Additive Models. We will investigate splines and multivariate adaptive regression splines (MARS), as well asensemble techniques like model stacking and model blending, and evaluate these models for the best results.

**Aim**
This data science project aims to build and evaluate different predictive models and determine the sales of each product at a particular store. This analysis will help BigMart understand the properties of products and stores, which are crucial in increasing sales and developing better business strategies.

**Deployment**
The entire training code was deployed on Dagster for automated refreshment and application. The assets.py file contains the code for deploying the model on Dagster.

**Data Description**
The BigMart sales prediction dataset contains 2013's annual sales records for 1559 products across ten stores in different cities. Such vast data can reveal insights about apparent customer preferences as a specific product and store attributes have been
defined in the dataset.
● item_identifier: unique identification number for particular items
● item_weight: weight of the items
● item_fat_content: fat content in the item such as low fat and regular fat
● item_visibility: visibility of the product in the outlet
● item_type: category of the product such as Dairy, Soft Drink, Household, etcs
● item_mrp: Maximum retail price of the product
● outlet_identifier: unique identification number for particular outlets
● outlet_establishment_year: the year in which the outlet was established
● outlet_size: the size of the outlet, such as small, medium, and high
● outlet_location_type: location type in which the outlet is located, such as Tier 1, 2
and 3
● outlet_type: type of the outlet such as grocery store or supermarket
● item_outlet_sales: overall sales of the product in the outlet

**Tech Stack**
Language: Python
Libraries: Pandas, NumPy, matplotlib, sklearn, redshift connector, Pyearth,
Pygam
