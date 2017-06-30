import tweepy

from app.models.twitter import auth
from app.models.twitter import utils


def get_friends(username):
    api = auth.get_api()
    return api.friends(screen_name=username, include_user_entities='false',
                       skip_status='true')


def screen_names_of_friends(username):
    friends = get_friends(username)
    return [user.screen_name for user in friends]


def search(query, count, sinceId=None):
    api = auth.get_api()
    results = []
    print(query)
    for tweet in tweepy.Cursor(api.search, q=query).items(40):
        result = {}
        result['screen_name'] = tweet.user.screen_name
        result['created_at'] = tweet.created_at
        result['text'] = tweet.text
        result['id'] = tweet.id_str
        result['video'] = (tweet.entities.get('urls') or [{}])[0].get('expanded_url')
        results.append(result)
    return results
