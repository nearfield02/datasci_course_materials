import sys
import json
import operator 

def gettweet(rawtweet):
    tweet = json.loads(rawtweet)
    if "entities" in tweet and "hashtags" in tweet["entities"]:
        return tweet["entities"]["hashtags"]

def updatehashtagcount(hashtags, htags):
    if not hashtags:
        return

    for tag in hashtags:
        if "text" in tag:
            if tag["text"] in htags:
                htags[tag["text"]] += 1
            else:
                htags[tag["text"]] = 1
    
def main():
    tweet_file = open(sys.argv[1])
    htags = {}
    for l in tweet_file:
        hashtags = gettweet(l)
        updatehashtagcount(hashtags, htags)
    sorted_htags = sorted(htags.items(), key=lambda t:t[1], reverse=True)
    ii = 0
    for tag in sorted_htags:
        print "%s %s"%(tag[0].replace(" ", '%20').encode('utf-8'), float(tag[1]))
        ii += 1
        if ii == 10:
            break
        
        
if __name__ == '__main__':
    main()
