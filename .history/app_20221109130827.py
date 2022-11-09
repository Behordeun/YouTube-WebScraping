#%%
from apiclient.discovery import build #pip install google-api-python-client
from apiclient.errors import HttpError #pip install google-api-python-client
from oauth2client.tools import argparser #pip install oauth2client
import pandas as pd #pip install pandas
import matplotlib.pyplot as plt #pip install matplotlib
import os

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

#%%
DEVELOPER_KEY =  os.getenv('DEVELOPER_KEY')
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

#%%
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

#%%
# Call the search.list method to retrieve results matching the specified
 # query term.
search_response = youtube.search().list(
 q=options.q,
 type="video",
 part="id,snippet",
 maxResults=options.max_results
).execute()

#%%
videos = {}

#%%
# Add each result to the appropriate list, and then display the lists of
 # matching videos.
 # Filter out channels, and playlists.
for search_result in search_response.get("items", []):
 if search_result["id"]["kind"] == "youtube#video" or search_result["id"]['kind']=="youtube#commentThread":
 #videos.append("%s" % (search_result["id"]["videoId"]))
  videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]
  
#%%
#print "Videos:\n", "\n".join(videos), "\n"

#%%
s = ','.join(videos.keys())

#%%
videos_list_response = youtube.videos().list(
 id=s,
 part='id,statistics'
).execute()

#%%
#videos_list_response['items'].sort(key=lambda x: int(x['statistics']['likeCount']), reverse=True)
#res = pd.read_json(json.dumps(videos_list_response['items']))

#%%
res = []
for i in videos_list_response['items']:
 temp_res = dict(v_id = i['id'], v_title = videos[i['id']])
 temp_res.update(i['statistics'])
 res.append(temp_res)
 
 #%%
 pd.DataFrame.from_dict(res)
 
 #%%
 myyoutube=pd.DataFrame.from_dict(res)
 
 #%%
 myyoutube.iloc[39]
 
 #%%
 