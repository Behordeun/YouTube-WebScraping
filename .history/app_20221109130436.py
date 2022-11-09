#%%
from apiclient.discovery import build #pip install google-api-python-client
from apiclient.errors import HttpError #pip install google-api-python-client
from oauth2client.tools import argparser #pip install oauth2client
import pandas as pd #pip install pandas
import matplotlib.pyplot as plt #pip install matplotlib

#%%
# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
# https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.

#%%
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--q",type=str,help="Search term", default="Ibaka TV")
#change the default to the search term you want to search
parser.add_argument("--max-results",type=int, help="Max results", default=150)
#default number of results which are returned. It can vary from 0 - 100
args,_ = parser.parse_known_args()
options = args