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
    txt = ""
    coord = ""
    user = ""
    place = ""
    if "text" in tweet:
        txt = tweet["text"]
    if "coordinates" in tweet:
        coord = tweet["coordinates"]
    if "user" in tweet:
        user = tweet["user"]
    if "place" in tweet:
        place = tweet["place"]
    return txt, coord, place, user

def updatestate(tweet, scores, state, happiest_states):
    sentimentscores = []
    words = tweet.split()
    score = 0
    for word in words:
        word = re.sub(r'[^a-zA-Z]', '', word)
        if word.lower() in scores:
            sentimentscores.append(scores[word.lower()])
       
    if len(sentimentscores):
        score = float(sum(sentimentscores))/float(len(sentimentscores))

    if score > 0.0:
        if state in happiest_states:
            happiest_states[state] += 1
        else:
            happiest_states[state] = 1
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = createdict(sent_file)
    happiest_states = {}
    for l in tweet_file:
        txt, coord, place, user = gettweet(l)
        if place and "country_code" in place and place["country_code"] == "US":
            full_name = place["full_name"].encode('utf-8').split(",")
            state = full_name[1].replace(" ", "")
            if txt and len(state) == 2:
                updatestate(txt, scores, state, happiest_states)
    max = 0
    hap_state = ""
    for state in happiest_states:
        if happiest_states[state] > max:
            max = happiest_states[state]
            hap_state = state
    print hap_state 
                
if __name__ == '__main__':
    main()
