import sys
import csv
import urllib
import json
import string
import re

debug = None
 
def sentiment(a,d):
    if a.lower() in d:
        return(float(d[a]))
    return 0

def main():
#
# Read the sentiment file into a dictionary.
#
    if len(sys.argv) != 3:
       if (debug): print len(sys.argv)
       return
    sent_file = open(sys.argv[1])
    with sent_file as f:
        r = (l.split('\t') for l in f)
        d = { row[0]:row[1] for row in r }

#
# Test cases.
#
        if (debug):    print "absentee", sentiment("absentee",d)
        if (debug):    print "jim", sentiment("jim",d)

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
#
# I think there's a fundamental bug in the way the problem is stated as
# when you look through the sentiment index, several (15) are comprised of
# two words. 
#
               #  words = re.findall(r'\w+',t) # string.split(t)
               #  words = re.findall(r"[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+",t)
                words = re.findall("[^\s]+",t)
                for j in words:
                   s = s + sentiment(j,d)
                   if debug: print j, sentiment(j,d)
                if (debug): print i,len(words),s, t
                print s
            except KeyError: 
                print s # pass

if __name__ == '__main__':
    main()
