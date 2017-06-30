import os
import tweepy

api_handle = None


def get_authorization():
    TWITTER_API_KEY = os.getenv('TWITTER_API_KEY', None)
    TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET', None)

    auth = tweepy.AppAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    return auth


def get_api():
    global api_handle

    if api_handle:
        return api_handle

    print("Connecting to twitter.")
    auth = get_authorization()
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    if (not api):
        raise Exception("Cannot connect to twitter using provided credentials")

    api_handle = api
    return api
