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
    words = tweet.split()
    new = []
    neg = False
    pos = False
    for word in words:
        word = re.sub(r'[^a-zA-Z@]', '', word)
        if word.lower() in scores:
            if scores[word.lower()] < 0.0:
                neg = True
            elif scores[word.lower()] > 0.0:
                pos = True
        else:
            if word != "":
                new.append(word)

    # assign positive or negative count to new terms       
    for term in new:
        if term in newterms:
            newterms[term][0] += 1.0 if pos is True else 0.0
            newterms[term][1] += 1.0 if neg is True else 0.0
        else:
            newterms[term] = []
            newterms[term].append(1.0 if pos is True else 0.0)
            newterms[term].append(1.0 if neg is True else 0.0)
            
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = createdict(sent_file)
    newterms = {}
    for l in tweet_file:
        tweet = gettweet(l)
        if tweet:
            getsentimentscore(tweet, scores, newterms)

    # winging it as the problem instructions are vague
    for term in newterms:
        if newterms[term][0] == 0.0:
            print "%s %.8f"%(term.replace(' ','%20'.encode('utf-8')), 0.0)
        elif newterms[term][1] == 0.0:
            print "%s %.8f"%(term.replace(' ','%20'.encode('utf-8')), 1.0)
        else:
            print "%s %.8f"%(term.replace(' ','%20'.encode('utf-8')),newterms[term][0]/newterms[term][1])

if __name__ == '__main__':
    main()
