-- Write a SQL statement to find all documents that have more than 300 
-- total terms, including duplicate terms.
--
SELECT count(docid) from (
select docid, sum(count)
FROM frequency
group by docid
having sum(count) > 300
)
;
