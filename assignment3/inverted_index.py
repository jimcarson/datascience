import MapReduce
import sys

"""
Inverted Index

The input is a two-element list: [document_id, text].  The document text may have words in upper or lower case and may contain punctuation.  Each token is treated as if it was a valid word.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# 
# Make the word list unique & preserve order.  
# Source: peterbe.com/plog/uniquifiers-benchmark
#
def uniqueify(seq, idfun=None): 
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result


def mapper(record):
    document_id = record[0]
    document_contents = record[1]
    words = document_contents.split()
    for w in uniqueify(words):
      mr.emit_intermediate(w, document_id)

def reducer(word, list_of_document_ids):
    doclist = []
    for v in list_of_document_ids:
      doclist.append(v)
    mr.emit((word, doclist))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
