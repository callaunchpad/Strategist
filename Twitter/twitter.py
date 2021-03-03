import tweepy

# Authenticate to Twitter
consumer_key = "WHZ42oEtUPTxR8Ga9V37yLlam"
consumer_secret = "Dk8htMfjCnmGyGfN269MHr9Da4Cy2LQer890kA9mjlwTE0CSh8"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)



# api.search returns a list of COUNT searchtweet objects.
# searchtweet object documentation & attributes: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet
# 
def searchTweet(ticker):
    result = api.search(q = ticker, lang = "en", count = 5, result_type = "recent")
    result = [r.text for r in result]
    return result


def main():
    tweets = searchTweet("TSLA")
    for tweet in tweets:
        print(tweet, '\n')

if __name__ == "__main__":
    main()





