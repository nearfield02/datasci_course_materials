import json

def printtweet(rawtweet):
    tweet = json.loads(rawtweet)
    if "text" in tweet:
        print tweet["text"]

f = open("tweets", "r")
for l in f:
    printtweet(l)
