#!/bin/bash

# This script perform retrival of parsedFiles/queries queries

echo "\n\n ------ RETRIVAL ------ \n"

# Clean results directory
if [ -d "./terrier/var/results" ];
then
    rm -rf terrier/var/results
fi
mkdir terrier/var/results

# List of possible parameters:
#   -D <property>                    specify property name=value
#   -q,--queryexpansion              apply query expansion to all queries
#	-t,--topics <topics>             specify the location of the topics file
#   -w,--wmodel <wmodel>             allows the default weighting model to be specified
sh terrier/bin/terrier batchretrieve \
	-w BM25 \
	-t parsedFiles/queries \
	-q 