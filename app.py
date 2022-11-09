# %% Import necessary libraries
from apiclient.discovery import build
from apiclient.errors import HttpError 
from oauth2client.tools import argparser 
import pandas as pd  # pip install pandas
import matplotlib.pyplot as plt  # pip install matplotlib
import argparse
import os

# %% Specify the target channel name
channel_name = input("Please type in the targeted channel name here: ")
parser = argparse.ArgumentParser()
parser.add_argument("--q", type=str, help="Search term",
                    default=f"{channel_name}")

parser.add_argument("--max-results", type=int, help="Max results", default=100)
# default number of results which are returned. It can vary from 0 - 100
args, _ = parser.parse_known_args()
options = args

# %% Supply the needed credentials to connect with the YouTube API
DEVELOPER_KEY = os.getenv('DEVELOPER_KEY')
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# %% Initiate the build job
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)

# %%
# Call the search.list method to retrieve results matching the specified
# query term.
search_response = youtube.search().list(
    q=options.q,
    type="video",
    part="id,snippet",
    maxResults=options.max_results
).execute()

# %% Create and empty dictionary to hold the scraped data
videos = {}

# %%
# Add each result to the appropriate list, and then display the lists of
# matching videos.
# Filter out channels, and playlists.
for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video" or search_result["id"]['kind'] == "youtube#commentThread":
        #videos.append("%s" % (search_result["id"]["videoId"]))
        videos[search_result["id"]["videoId"]
               ] = search_result["snippet"]["title"]

# %%
s = ','.join(videos.keys())

# %%
videos_list_response = youtube.videos().list(
    id=s,
    part='id,statistics'
).execute()

# %%
res = []
for i in videos_list_response['items']:
    temp_res = dict(v_id=i['id'], v_title=videos[i['id']])
    temp_res.update(i['statistics'])
    res.append(temp_res)

# %% Converted the scraped data into a DataFrame
myyoutube = pd.DataFrame.from_dict(res)

# %%
myyoutube.to_csv(f"{channel_name}.csv", index=False, header=True)

# %%
