from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import json
import ScreenGraphic
import ComputeTweets

ScreenGraphic.printTitle()

name = input("What is the name of the user you are looking for? or Press Q to Quit").strip()

ComputeTweets.openFiles("opinion-lexicon-English/positive-words.txt", "opinion-lexicon-English/negative-words.txt")

while(name.lower() != "q"):
    ComputeTweets.compute(name)
    name = input("\n\nWhat is the name of the next user you are looking for? or Press Q to Quit").strip()

print("\nThanks For Trying My Program!! :)")
