import MapReduce
import sys

"""
Relational join - Jim Carson

     SELECT * 
     FROM Orders, LineItem 
     WHERE Order.order_id = LineItem.order_id

Sample input:
["order", "1", "36901", "O", "173665.47", "1996-01-02", "5-LOW", "Clerk#000000951", "0", "nstructions sleep furiously among "]

["line_item", "1", "63700", "3701", "3", "8", "13309.60", "0.10", "0.02", "N", "
O", "1996-01-29", "1996-03-05", "1996-01-31", "TAKE BACK RETURN", "REG AIR", "ri
ously. regular, express dep"]

The first field indicates what type of record, second field is the order_id.
Combination should have 27 
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(order_id, row):
    l=len(row)
    # since the zeroeth element is the record type identifier, start with ID
    for i in range(1,l):
      v = []
      v += row[0] # order_id
      v += row[i] # Joined row
      mr.emit(v)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
