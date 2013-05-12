--
-- Express A X B as a SQL query.  REturn just the value of cell (2,3)
--
--
select v from (
SELECT A.row_num, B.col_num, SUM(A.value * B.value) as v
  FROM A, B
 WHERE A.col_num = B.row_num
 GROUP BY A.row_num, B.col_num
)
where row_num = 2 and col_num = 3
;
