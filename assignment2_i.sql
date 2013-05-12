-- Find the best matching document to the keyword query
-- "washington taxes treasury".
-- ;
create table if not exists q ( kw varchar(20) );
insert into q values('washington');
insert into q values('taxes');
insert into q values('treasury');

select max(v) as similarity from (
SELECT A.docid, B.docid as b, SUM(A.count) as v
  FROM frequency as A join frequency as B on A.term = B.term
 WHERE
 A.docid < B.docid
 and a.term in (select kw from q) -- ('washington','taxes','treasury')
 and b.term in (select kw from q) -- ('washington','taxes','treasury')
-- Since we're limiting ourselves to a specific set of documents,
-- our query is faster
 GROUP BY A.docid, B.docid
)
;
