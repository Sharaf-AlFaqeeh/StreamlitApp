import os
from deta import Deta # pip install deta
from dotenv import load_dotenv # to store the key  to be hidden
# dete site key 
# load environment variables
load_dotenv(".env")
# DETA_KEY = "my_deta_key" #this will be change to bellow
DETA_KEY = os.getenv("DETA_KEY") #this DETA_KEY variable is in the dotenv file .env

deta =Deta(DETA_KEY) 


db = deta.Base("monthly_reports")

def insert_period(period,incomes, expenses, comment):
    """Return the report on a successful creation, otherwise raises an error"""
    return db.put({"key":period ,"incomes":incomes, "expenses":expenses, "commint":comment})

def fetch_all_periods():
    """Return a dict of all period"""
    res = db.fetch()
    return res.items

def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)