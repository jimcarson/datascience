-- Write a SQL statement to count the number of documents containing the word “parliament”
SELECT count(distinct docid)
FROM frequency
where term = 'parliament'
;
