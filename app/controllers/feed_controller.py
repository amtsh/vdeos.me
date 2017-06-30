from app.models.twitter import Twitter


def get_video_feed(username):
    keyword = 'youtube.com'
    screen_names = Twitter.screen_names_of_friends(username)
    print("{} friends found for account : {}".format(len(screen_names), username))

    from_accounts = ['from:{}'.format(screen_name) for screen_name in screen_names]
    from_accounts_query = ', OR '.join(from_accounts)
    query = keyword + ' ' + from_accounts_query

    return Twitter.search(query, 100)
