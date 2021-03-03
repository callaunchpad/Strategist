import tweepy

# Authenticate to Twitter
consumer_key = "WHZ42oEtUPTxR8Ga9V37yLlam"
consumer_secret = "Dk8htMfjCnmGyGfN269MHr9Da4Cy2LQer890kA9mjlwTE0CSh8"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
# test authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def searchTweet(ticker):
    print(api.search(q = ticker, lang = "en", count = 5, result_type = "recent"))


def main():
    print(searchTweet("TSLA"))

if __name__ == "__main__":
    main()





