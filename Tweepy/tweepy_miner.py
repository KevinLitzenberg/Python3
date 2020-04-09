import json
import pandas as pd
from SecretsManger import configManager
from TweepyMiner import TweetMiner

if __name__=="__main__":

    PasswordManager = configManager("secrets.cfg")

    user_keys = {
       'consumer_key':        PasswordManager.get_config_value("keys","consumer_key"),
       'consumer_secret':     PasswordManager.get_config_value("keys","consumer_secret"),
       'access_token_key':    PasswordManager.get_config_value("tokens","access_token"),
       'access_token_secret': PasswordManager.get_config_value("tokens","access_token_secret")
    }

    Miner = TweetMiner(result_limit = 200, keys_dict=user_keys)

    mined_tweets = Miner.mine_user_tweets(user='dril', max_pages=17)

    mined_tweets_df = pd.DataFrame(mined_tweets)

    print(mined_tweets_df)
else:
    print("Module is being imported")
