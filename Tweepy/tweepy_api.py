import json
from SecretsManger import configManager
import tweepy

def serialize_json(json_tweepy_obj):

    # convert to string
    json_str = json.dumps(json_tweepy_obj._json)

    # deserialize string into python object
    json_py_obj = json.loads(json_str)
    
    return json_py_obj

def print_json(json_py_str):
    print(json.dumps(json_py_str, indent=4, sort_keys=True))




def user_checkout(user):
    #pp.pprint(f'user: {user}')
    print(f"id: {user['id']}")
    print(f"name: {user['name']}")
    print(f"screen_name: {user['screen_name']}")
    print(f"statuses count: {user['statuses_count']}")
    #print(f"friends : {user['friends']}")

def print_tweets(user):
   for tweet in user:
      pp.pprint(tweet.tweet)

# Example using tweepy Cursors
def get_public_tweets(user_id):
   for status in tweepy.Cursor(api2.user_timeline, id=user_id).items():
      #pprint(page[0]['text'])
      print(f"{status['text']}")
      #for tweet in item:
          #status = item
          #print(f"{item}")
          #json_str = json.dumps(status['tweet'])
          #print(f"{json_str}")

def get_status(user):
    status_list = api.user_timeline(user)
    status = status_list[0]   
    json_str = json.dumps(status['text'])
    #pp.pprint(f'{json.dumps(status)}')
    print(f"{json_str}")



if __name__=="__main__":

    # create a password manager object
    PasswordManager = configManager("secrets.cfg")

    twitter_keys = {
        'consumer_key':        PasswordManager.get_config_value("keys","consumer_key"),
        'consumer_secret':     PasswordManager.get_config_value("keys","consumer_secret"),
        'access_token_key':    PasswordManager.get_config_value("tokens","access_token"),
        'access_token_secret': PasswordManager.get_config_value("tokens","access_token_secret")
    }

    #Setup access to API
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

    api = tweepy.API(auth)

    #Make call on home timeline, print each tweets text
    public_tweets = api.user_timeline('Sidewalks_Jake')
    for tweet in public_tweets:
        print(tweet.text)
    
    print_json(serialize_json(public_tweets[0]))    

    

    print(f"public_tweets[0]: {public_tweets[0]}")

