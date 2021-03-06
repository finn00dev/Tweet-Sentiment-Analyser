import urllib

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import json
import string

ACCESS_KEY = "1074796956-K2giYLUhgbktbQZ5W7PI5rO9ztwrvlFxVXkoFse";
ACCESS_KEY_SECRET = "CxwOUfMx68JrbvcodHXJxqkirzUvYOk2F1SPrhC3pzKE5";
CONSUMER_KEY = "5hJaPQlDj9Df607bQBK3ElHQn";
CONSUME_KEY_SECRET = "06NyEpwV4OHVHlXuBob2NCQjd7jYMqXJzfPBmU0FD67IFDKixX";

twitter = Twitter(auth=
                  OAuth(ACCESS_KEY,
                        ACCESS_KEY_SECRET,
                        CONSUMER_KEY,
                        CONSUME_KEY_SECRET
                        )
                  )

pos = []
neg = []
PUNC = "!#$%&*^()_|\}]{[\"\':;?/>.<,"

def openFiles(pos_keywords, neg_keywords):
    pos_file = open(pos_keywords, "r")
    pos_file.readline()

    for word in pos_file:
        pos.append(word.strip())

    pos_file.close()

    neg_file = open(neg_keywords, "r")
    neg_file.readline()

    for word in neg_file:
        neg.append(word.strip())

    neg_file.close()

def tweetsToArray(userName):
    output = twitter.statuses.user_timeline(screen_name=userName)
    array = []

    for tweet in output:
        if str(tweet["text"][0:2]) != "RT":
            tweet_full = ""
            for word in tweet["text"].split():
                tweet_full += word.lower() + " "
            array.append(tweet_full)

    return array

def analyseTweet(tweet):
    value = 0
    output = [[], []]
    for word in tweet.split():
        if word.strip(PUNC) in pos:
            value += 1
            output[0].append(word)
        elif word.strip(PUNC) in neg:
            value -= 1
            output[1].append(word)
    output.append(value)
    return output

def doesUserExsist(name):
    try:
        test = twitter.users.lookup(screen_name=name)
        return True
    except TwitterHTTPError as err:
        return False

def compute(userName):

    tweets_printed = 0

    if(doesUserExsist(userName)):
        tweets = tweetsToArray(userName)
        for tweet in tweets:
            output = analyseTweet(tweet)
            if len(output[0]) > 0 and len(output[1]) > 0:
                tweets_printed = tweets_printed + 1
                print(tweet)
                print("positive:")
                for word in output[0]:
                    print(word, "1")
                print("negative:")
                for word in output[1]:
                    print(word, "-1")
                print("Total Value =", output[2], "\n")

        if tweets_printed == 0:
            print("\nNo Recent Tweets With Sentiment Found")

    else:
        print("\nUser Does Not Exist")


