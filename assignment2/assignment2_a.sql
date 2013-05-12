-- Write a query that's equivalent to:
--
-- σdocid=10398_txt_earn(frequency)
--
-- For this, were' just turning in the count.
SELECT count(*) FROM frequency where docid like '10398_txt_earn';
