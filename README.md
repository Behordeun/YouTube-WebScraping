# YouTube-WebScraping

## About the App

The app allows users to scrape data from [YouTube](https://www.youtube.com) simply by making use of the ***Google YouTube API***. It allows users to specify a channel of interest whose data they want to scrape. It fetches 50 most recent videos from the channel with the following features:

* Video ID (v_id)
* Video title (v_title)
* Number of Views (viewCount)
* Number of Likes (likeCount)
* Number of Favorites (favoriteCount) and
* Number of Comments (commentCount)

It thereafter converts the scraped data into a CSV file which can be used for further analytics

### How to Use the App

Run the following commands on your terminal

1. First clone this repository into a directory of choice by running `git clone https://github.com/Behordeun/YouTube-WebScraping.git`
2. Therafter navigate to the cloned directory `cd YouTube-WebScraping`
3. create a file **.env** `touch .env`; paste in your **YouTube API** key into the created environment variable. It should look like this `DEVELOPER_KEY = 'YOURKEY'`
4. Install the dependencies by running `pip install -r requirements.txt` or `python -m pip install -r requirements.txt`
5. Run this command `Python app.py`

You will get a prompt from your terminal to type in the target channel name, and voila, the data will be scrapped shortly, and you can find the converted CSV file the current directory.

## About Me

Muhammad Abiodun SULAIMAN is a data analytics professional with an extensive experience of over four years in developing algorithms to help make raw data more useful to enterprises. Strong background in a signiﬁcant set of technical skills, including a deep knowledge of System Design, SQL database design, AWS, Microsoft Azure, and many more cloud computing databases.

I currently work at Tsaron Technologies Limited, an InsureTech startup company where I work as a one-man data team responsible for the design, build and deployment of an Artificial Intelligence (AI) powered driver scorecard system that scores, ranks and classify drivers into either of the available safety zones based off of their driving behaviour.

The purpose of this project is to understand, analyse and evaluate media campaigns by companies through youtube, thanks to AnalyticsVydia for the code snippet. I will be analysing the result of my queries with Microsoft PowerBI. I chose Infinix because I have been using the phone model for quite sometime now, and will like to explore their level of media engagement!!

Thanks for reading my code and you can as well run your code with google API. `</p>`

You can follow me on [LinkedIn](`https://www.linkedin.com/in/muhammad-abiodun-sulaiman`) or [Twitter](`www.twitter.com/Prince_Analyst`) or [Medium](https://www.medium.com/@behordeun) for more interestingarticles and projects from me.
