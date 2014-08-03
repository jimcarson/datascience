Instructions on how to run example.pig.
================================================================

Step 0: Clone the course repository.

     cd ~
     git clone https://github.com/uwescience/datasci_course_materials.git
 
Step 1: Install pig locally
     mkdir ~/pig
     cd ~/pig
     curl http://download.nextag.com/apache/pig/pig-0.13.0/pig-0.13.0.tar.gz -o pig-0.13.0.tar.gz
     tar xzvf pig-0.13.0.tar.gz 
     cd ~/datasci_course_materials/assignment4

Step 2: Grab a local copy of the files:

     cd ~/datascience/assignment4
     wget http://uw-cse-344-oregon.aws.amazon.com.s3.amazonaws.com/cse344-test-file

   *Warning* This file is 2Gb:
     wget http://uw-cse-344-oregon.aws.amazon.com.s3.amazonaws.com/btc-2010-chunk-000

Step 3: Run pig
     ~/pig/pig-0.13.0/bin/pig -x local
     grunt> run example.pig

Step 4: Profit!
