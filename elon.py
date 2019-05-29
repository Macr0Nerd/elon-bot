import random, tweepy

consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)


def user_tweet(thandle):
    statuses = api.user_timeline(screen_name=thandle, count=50, tweet_mode="extended")
    return statuses

def rand_elon():
    latest_tweet = user_tweet("elonmusk")
    random_tweet = random.choice(latest_tweet).full_text.split()

    for i in range(len(random_tweet)):
        if "&amp" in random_tweet[i]:
            random_tweet[i] = "&"

    for i in range(len(random_tweet)):
        if random_tweet[i][0] == "@":
            continue
        else:
            random_tweet = ' '.join(random_tweet[i:])
            break

    return random_tweet

if __name__ == "__main__":
    input(">> ")
    print(rand_elon())
