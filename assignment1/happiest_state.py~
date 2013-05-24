import sys
import json
import re

def createdict(sent_file):
    scores = {}
    for line in sent_file:
        term,score = line.split("\t")
        scores[term.lower()] = int(score)
    return scores

def gettweet(rawtweet):
    tweet = json.loads(rawtweet)
    if "text" in tweet:
        return tweet["text"]

def getsentimentscore(tweet, scores, newterms):
    sentimentscores = []
    words = tweet.split()
    for word in words:
        word = re.sub(r'[^a-zA-Z]', '', word)
        if word.lower() in scores:
            sentimentscores.append(scores[word.lower()])
       
    if len(sentimentscores):
        return float(sum(sentimentscores))/float(len(sentimentscores))
    else:
        return 0
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = createdict(sent_file)
    newterms = {}
    for l in tweet_file:
        tweet = gettweet(l)
        if tweet:
            s = getsentimentscore(tweet, scores, newterms)
            print s

if __name__ == '__main__':
    main()
