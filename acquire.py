import pandas as pd
import os
from env import get_db_url

#########
# Retrieves the titanic dataset either from the codeup server or a csv if its already been imported

def get_titanic_data():
    url = get_db_url('titanic_db')
    query = 'SELECT * FROM passengers;'
    filename = 'titanic.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql(query, url)
        df.to_csv(filename)
        return df
        
##########
# Retrieves the iris dataset either from the codeup server or a csv if its already been imported

def get_iris_data():
    url = get_db_url('iris_db')
    query = '''SELECT * 
               FROM species
               JOIN measurements
               ON species.species_id=measurements.species_id;'''
    filename = 'iris.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql(query, url)
        df.to_csv(filename)
        return df
        
##########
# Retrieves the telco dataset either from the codeup server or a csv if its already been imported

def get_telco_data():
    url = get_db_url('telco_churn')
    query = '''SELECT * 
             FROM customers
             JOIN payment_types USING (payment_type_id)
             JOIN contract_types USING (contract_type_id)
             JOIN internet_service_types USING (internet_service_type_id);'''
    filename = 'telco.csv'
             
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql(query, url)
        df.to_csv(filename)
        return df