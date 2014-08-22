--
-- Filter+inner/self-Join, small file.
--
register ./pigtest/myudfs.jar

raw = load './cse344-test-file.txt' USING TextLoader as (line:chararray);

-- Flatten
tmp = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- Filter
ff = filter tmp by (subject matches '.*business.*');

f = DISTINCT ff;

store f into 'p3a_preliminary' using PigStorage();

-- Copy filtered list
ftmp = foreach f GENERATE * as (subject2:chararray,predicate2:chararray,object2:chararray);
f2 = distinct ftmp PARALLEL 50;

-- Join
j = JOIN f by subject , f2 by subject2 PARALLEL 50;

-- remove duplicates
result = distinct j PARALLEL 50;

-- emit results
store result into 'p3a_result' using PigStorage();
