-- Write a SQL statement to count the number of unique documents that -- contain both the word 'transactions' and the word 'world'.
SELECT count(distinct docid)FROM frequency
where term = ( 'world' )
and docid in (
select distinct docid from frequency
where term in ( 'transactions' )
)
;
