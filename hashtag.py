import json, sys

def main():
    all_terms = 0
    termlist = {}
    for record in [json.loads(line) for line in open(sys.argv[1]).readlines()]:
        tmp = record.get('entities')
        if tmp != None:
            hash = tmp.get('hashtags')
            if len(hash) > 0:
               for h in hash:
                   if len(h) > 0:
                      tag = h.get('text')
#                      print tag
                      if len(tag) > 0:
                         all_terms += 1
                         if not tag in termlist:
		             termlist[tag] = 0
		         termlist[tag] = termlist[tag] + 1
    
    sorted_score = sorted(termlist.items(), key = lambda term: term[1], reverse=True)
    for term in sorted_score[0:10]:
	print term[0], "%6.3f" %float(term[1]) 


def getWords(tweet):
    return [term.strip().encode('utf-8') for term in tweet.split()]

if __name__ == '__main__':
    main()
