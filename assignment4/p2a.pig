register ./pigtest/myudfs.jar
raw = load './cse344-test-file.txt' USING TextLoader as (line:chararray);
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- cluster by subject
subjects = group ntriples by (subject) PARALLEL 20;

count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;

-- Produce unique tuples.
histogram = group count_by_subject by (count) PARALLEL 50;

-- emit output.
store histogram into 'p2a_histogram' using PigStorage();

