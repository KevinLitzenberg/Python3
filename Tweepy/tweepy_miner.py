import argparse
import importlib
import json
import logging
import os
import pandas as pd
from SecretsManger import configManager
import sys
from TweepyMiner import TweetMiner

def create_key_dict(PasswordManager):
    user_keys = {
       'consumer_key':        PasswordManager.get_config_value("keys","consumer_key"),
       'consumer_secret':     PasswordManager.get_config_value("keys","consumer_secret"),
       'access_token_key':    PasswordManager.get_config_value("tokens","access_token"),
       'access_token_secret': PasswordManager.get_config_value("tokens","access_token_secret")
    }
    return user_keys
    
def debug_panda_object(pd_object):
    logging.debug(f"Panda Object:")
    logging.debug(f"pd_object :\n{pd_object}")
    logging.debug(f"\n\n")

def debug_panda_object_charactoristics(pd_object):
    logging.debug(f"Object Characteristics:")
    logging.debug(f"pd_object.head() :\n{pd_object.head()}")
    logging.debug(f"type(pd_object) : {type(pd_object)}")
    logging.debug(f"pd_object.shape : {pd_object.shape}")
    logging.debug(f"\n\n")

def get_tweets(df):
    for i in df.items():
        print(df['text'])

if __name__=="__main__":

    PasswordManager = configManager("secrets.cfg")

    #user_keys = {
    #   'consumer_key':        PasswordManager.get_config_value("keys","consumer_key"),
    #   'consumer_secret':     PasswordManager.get_config_value("keys","consumer_secret"),
    #   'access_token_key':    PasswordManager.get_config_value("tokens","access_token"),
    #   'access_token_secret': PasswordManager.get_config_value("tokens","access_token_secret")
    #}
    user_keys = create_key_dict(PasswordManager)

    Miner = TweetMiner(result_limit = 200, keys_dict=user_keys)

    mined_tweets = Miner.mine_user_tweets(user='dril', max_pages=17)

    mined_tweets_df = pd.DataFrame(mined_tweets)

    print(mined_tweets_df)
#else:
print("Module tweepy_miner is being imported.")

def print_df_columns(df):
   print(df.columns)

PasswordManager = configManager("secrets.cfg")
user_keys = create_key_dict(PasswordManager)
PasswordManager.print_config_key("keys","consumer_key")
Miner = TweetMiner(result_limit = 200, keys_dict=user_keys)
mined_tweets = Miner.mine_user_tweets(user='dril', max_pages=17)
mined_tweets_df = pd.DataFrame(mined_tweets)
#print_df_columns(tweepy_miner.mined_tweets_df)
#print_df_columns(tm.mined_tweets_df)
#df_selector = tweepy_miner.mined_tweets_df[(tweepy_miner.mined_tweets_df['quote_text'] != 'None')]
	
