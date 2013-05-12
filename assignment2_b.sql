-- Write a SQL query that's equivalent to the following relational
-- algebra expression:
-- πterm( σdocid=10398_txt_earn and count=1(frequency))
-- Again, we're turning in only the count.
SELECT count(*) FROM frequency where docid = '10398_txt_earn' and count = 1;
