import sys,json
import csv
import urllib
import string
import re

debug = None

# from:
# http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/
# but I used a regexp to reverse it.
states = { 'Alaska' : 'AK', 'Alabama' : 'AL', 'Arkansas' : 'AR', 'Arizona' : 'AZ', 'California' : 'CA', 'Colorado' : 'CO', 'Connecticut' : 'CT', 'District of Columbia' : 'DC', 'Delaware' : 'DE', 'Florida' : 'FL', 'Georgia' : 'GA', 'Guam' : 'GU', 'Hawaii' : 'HI', 'Iowa' : 'IA', 'Idaho' : 'ID', 'Illinois' : 'IL', 'Indiana' : 'IN', 'Kansas' : 'KS', 'Kentucky' : 'KY', 'Louisiana' : 'LA', 'Massachusetts' : 'MA', 'Maryland' : 'MD', 'Maine' : 'ME', 'Michigan' : 'MI', 'Minnesota' : 'MN', 'Missouri' : 'MO', 'Mississippi' : 'MS', 'Montana' : 'MT', 'National' : 'NA', 'North Carolina' : 'NC', 'North Dakota' : 'ND', 'Nebraska' : 'NE', 'New Hampshire' : 'NH', 'New Jersey' : 'NJ', 'New Mexico' : 'NM', 'Nevada' : 'NV', 'New York' : 'NY', 'Ohio' : 'OH', 'Oklahoma' : 'OK', 'Oregon' : 'OR', 'Pennsylvania' : 'PA', 'Puerto Rico' : 'PR', 'Rhode Island' : 'RI', 'South Carolina' : 'SC', 'South Dakota' : 'SD', 'Tennessee' : 'TN', 'Texas' : 'TX', 'Utah' : 'UT', 'Virginia' : 'VA', 'Virgin Islands' : 'VI', 'Vermont' : 'VT', 'Washington' : 'WA', 'Wisconsin' : 'WI', 'West Virginia' : 'WV', 'Wyoming' : 'WY' }
happiness = {}
 
def get_state(t):
    place = t.get('place')
    if place != None:
	if place.get('country_code') == u'US': 
	    if place.get('place_type') == 'admin':
	        return states[place.get('name')]
    return None

def sentiment(a,d):
    if a.lower() in d:
        return(float(d[a]))
    return 0

def lines(fp):
    if (debug): print str(len(fp.readlines()))

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
# Read tweet file
#

    tweet_file = open(sys.argv[2])
    with tweet_file as f:
        response = f.readlines()

        for i in range(len(response)):
            s = 0
            pyresponse = json.loads(response[i])
            state = get_state(pyresponse)
            if state <> None:
                try:
                    t = pyresponse["text"].encode("utf-8")
#  words = re.findall(r"[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+",t)
                    words = re.findall("[^\s]+",t)
                    for j in words:
                       s = s + sentiment(j,d)
                       if debug: print j, sentiment(j,d)
                    if (debug): print i,len(words),s, t
                    # print s
                    # print state, states[state]
                    if state in happiness:
                        happiness[state] = happiness[state] + s
                    else:
                        happiness[state] = s
                except KeyError: pass
        #    print lines(sent_file)
    sorted_score = sorted(happiness.items(), key = lambda term: term[1], reverse=True)
    for term in sorted_score[0:1]:
        print term[0] # , "%6.3f" %float(term[1])
      
if __name__ == '__main__':
    main()
