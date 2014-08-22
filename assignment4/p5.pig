--
-- Filter+inner/self-Join, medium file.  The instructions are horribly
-- confusing.
--
register ./pigtest/myudfs.jar

raw = load './btc-2010-chunk-000' USING TextLoader as (line:chararray);

-- Flatten
tmp = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- Filter
ff = filter tmp by (subject matches '.*rdfabout\\.com.*');

f = DISTINCT ff;

-- store f into 'p5_preliminary' using PigStorage();

-- Copy filtered list
ftmp = foreach f GENERATE * as (subject2:chararray,predicate2:chararray,object2:chararray);
f2 = distinct ftmp;

-- Join
j = JOIN f by object , f2 by subject2;

-- remove duplicates
result = distinct j;

-- emit results
store result into 'p5_result' using PigStorage();
