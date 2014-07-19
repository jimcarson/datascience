import MapReduce
import sys

"""
Unique trims

Consider a set of key-value pairs where each key is sequence id and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....
Remove the last 10 characters from each string then remove any duplicates.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # Since we're only using the sequence, we'll just trim the last ten
    # characters 
    trimmed_sequence = (record[1])[:-10]
    mr.emit_intermediate(trimmed_sequence, 0)

def reducer(sequence, list_of_values):
    mr.emit((sequence))  # No, really, that's it.

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
