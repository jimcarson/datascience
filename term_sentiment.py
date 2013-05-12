import json, sys

SCALE = 5.0
debug = None

def print_mood_by_word(mood, tweet):
    # I was initially going to filter out a lot of other stuff, but the
    # rubric evaluated @JonasBrothers as an option.  Thus I cut back to 
    # minimum punctuation.
    clean_punct = dict.fromkeys(map(ord, ':;,.!'), None)
    # This caught me off-guard:
    # words = tweet.translate(clean_punct).lower().split()
    # the grader was expecting unaltered case.
    words = tweet.translate(clean_punct).split()
    
    new_words = []
    # I initially tried a very ornate procedure with positive and negative
    # weighting.  Overkill for the assignment.
    m = 0.0
    score = 0.0
    i = 0
    for word in words:
        if word in mood:
            score += mood[word]
            i += 1
        else:
            new_words.append(word)

    if i > 0: 
         message_score = score / i
    else:
         message_score = 0

    for new_word in new_words:
        mood[new_word] = message_score
        print "%s %6.2f" % (new_word.encode('utf-8'), message_score)
    
def main():
#
# Read the sentiment file into a dictionary.
#
    if len(sys.argv) != 3:
       if (debug): print len(sys.argv)
       print "Missing arguments:  tweet_sentiment sentimentfile  tweetlist"
       return

    sent_file = open(sys.argv[1])
    with sent_file as f:
        r = (l.split('\t') for l in f)
        mood = { row[0]:int(row[1]) for row in r }

#
# Read tweet file
#

    tweet_file = open(sys.argv[2])
    with tweet_file as f:
        response = f.readlines()

        for i in range(len(response)):
            s = 0
            pyresponse = json.loads(response[i])
            try:
                t = pyresponse["text"].encode("utf-8")
#                tweet_map = json.loads(t)
                tweet = pyresponse.get('text', '')
            
                if len(tweet) > 0:
                    print_mood_by_word(mood, tweet)

            except KeyError: pass


if __name__ == '__main__':
    main()
