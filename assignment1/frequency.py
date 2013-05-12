import json, sys

def main():
    all_terms = 0
    termlist = {}
    for record in [json.loads(line) for line in open(sys.argv[1]).readlines()]:
	tweet = record.get('text')
	if tweet != None:
            terms = getWords(tweet)
            for w in terms:
#                print w
                if len(w) > 0:
                   all_terms += 1
                   if not w in termlist:
		       termlist[w] = 0
		   termlist[w] = termlist[w] + 1
    
    sorted_score = sorted(termlist.items(), key = lambda term: term[1])
    for term in sorted_score:
	print term[0], "%6.3f" %(float(term[1]) / all_terms)


def getWords(tweet):
    return [term.strip().encode('utf-8') for term in tweet.split()]

if __name__ == '__main__':
    main()
