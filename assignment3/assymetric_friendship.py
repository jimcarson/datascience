import MapReduce
import sys

"""
Asymmetric relationship detector

Input is a two-element list [personA, personB], representing a simple social network.  Note that friendship may not be bidirectional.  Show the ones that are not symmetric.

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate(personA, personB)

def reducer(personA, friendlist):
    for so_called_friend in friendlist:
       if so_called_friend not in mr.intermediate.keys() or personA not in mr.intermediate[so_called_friend]:
          mr.emit((personA,so_called_friend))
          mr.emit((so_called_friend,personA))
         
#    mr.emit((personA, len(friendlist)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
