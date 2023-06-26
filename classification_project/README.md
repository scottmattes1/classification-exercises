
***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___



Data Dictionary
------------------
Column Name                  Description
------------------------------------------------------------------------------
Unnamed: 0                   Index column (automatically generated)
internet_service_type_id     Identifier for the type of internet service
contract_type_id             Identifier for the type of contract
payment_type_id              Identifier for the payment type
customer_id                  Unique identifier for each customer
gender                       Customer's gender (Male or Female)
senior_citizen               Indicates if the customer is a senior citizen (0 or 1)
partner                      Indicates if the customer has a partner (Yes or No)
dependents                   Indicates if the customer has dependents (Yes or No)
tenure                       Number of months the customer has been with the company
...                           (Additional columns omitted for brevity)
tech_support                 Indicates if the customer has technical support (Yes or No)
streaming_tv                 Indicates if the customer has streaming TV service (Yes or No)
streaming_movies             Indicates if the customer has streaming movie service (Yes or No)
paperless_billing            Indicates if the customer has opted for paperless billing (Yes or No)
monthly_charges              Monthly charges for the services
total_charges                Total charges billed to the customer
churn                        Indicates if the customer has churned (Yes or No)
payment_type                 Type of payment (Mailed check, Electronic check, etc.)
contract_type                Type of contract (One year, Month-to-month, etc.)
internet_service_type        Type of internet service (DSL, Fiber optic, etc.)



Project Outline
-----------------
Follow the data science pipeline

PLANNING (FINISHED AND DISPLAYED HERE)
ACQUIRE
PREPARE
EXPLORATORY DATA ANALYSIS
MODEL
DEPLOY (PER USE CASE)



Key Findings
-----------------
What drives customer churn?

Two year contracts, month-to-month contracts, fiber optic internet, and electronic check payments drive customer churn and tracking this data will help identify customers at risk of churn through modeling

The Random Forest model produced the best results using these columns (77%, 4% above baseline; each percent represents 40 customers)



Steps to Reproduce
-----------------------
env file with credentials to access the codeup database

random seed = 123

copy the exact imports used in the final notebook and run the code
        




