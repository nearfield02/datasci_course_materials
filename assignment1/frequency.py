import sys
import json
import re

def gettweet(rawtweet):
    tweet = json.loads(rawtweet)
    if "text" in tweet:
        return tweet["text"]

def updatetermfrequencies(tweet, termfreq):
    words = tweet.split()
    for word in words:
        word = re.sub(r'[^a-zA-Z@]', '', word)
        if word.lower() in termfreq:
            termfreq[word.lower()] += 1.0
        else:
            termfreq[word.lower()] = 1.0
            
def main():
    tweet_file = open(sys.argv[1])
    termfreq = {}
    overalltermcount = 0.0
    for l in tweet_file:
        tweet = gettweet(l)
        if tweet:
            updatetermfrequencies(tweet, termfreq)

    for term in termfreq:
        overalltermcount += termfreq[term]

    for term in termfreq:
        print "%s %.8f"%(term.replace(' ','%20'.encode('utf-8')), termfreq[term]/overalltermcount)

if __name__ == '__main__':
    main()
