import MapReduce
import sys

"""
Friend Count

Input is a two-element list [personA, personB], representing a simple social network.  Note that friendship may not be bidirectional.  That is for the next exercise.

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate(personA, personB)

def reducer(personA, friendlist):
    mr.emit((personA, len(friendlist)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
