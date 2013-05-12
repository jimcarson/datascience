--
-- Write a query to compute the similarity matrix D x DT.
-- create index i_term on frequency(term);
-- ;
select v from (
SELECT A.docid, B.docid, SUM(A.count * B.count) as v
  FROM frequency as A join frequency as B on A.term = B.term
 WHERE
 A.docid < B.docid
-- Since we're limiting ourselves to a specific set of documents,
-- our query is MUCH faster
and A.docid = '10080_txt_crude'
and B.docid = '17035_txt_earn'
 GROUP BY A.docid, B.docid
)
;
