from twitter_scraper import get_tweets


print(get_tweets('twitter', pages=1))
for tweet in get_tweets('twitter', pages=1):
    print(tweet)