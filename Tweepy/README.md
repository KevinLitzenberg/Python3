Tweepy API Python files:

Written using Python3.8: Uses f'strings so Python3.6 >, however not tested on any other version then 3.8.

SecretsManager: version 0.0.1
	* A class for managing Twitter API Keys and Tokens.
	* Expects a file called "secrets.cfg" to be in working directory.

Up and running:
1. python3.8 -m venv venv
2. pip3.8 install -r requirments.txt
3. source venv/bin/activate
4. vi secrets_example.cfg (update with credentials)
5. mv secrets_config.cfg secrets.cfg
6. Happy Pythoning!

Files:
tweepy_api.py : simple python script to explore the functionality of the tweepy package.
	* Takes a hardcoded user (Sidewalks_Jake of [Sidewalks and Selectons])
	* Pulls the latest status tweets.
	* Outputs in serialized json and plain output

tweepy_miner.py : Uses the Class TweepyMiner to create a tweepy api object and methods to perform operations on that object. 
	* Currently, using panda to visualize the data 
 

TweepyMiner.py : Class file used to create the tweepy api object interact with the Twitter API.
   	* TweetMiner initalizes a tweepy api object.
	* Methods:
		- mine_user_tweets: default user="dril"
		- uses some logic to follow retweets and quote_text
 
