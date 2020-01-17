#!/bin/bash

# This script perform retrieval & evaluation of "parsedFiles/queries"

echo "\n\n ------ DEFAULT RETRIEVAL ------ \n"

# Clean results directory
if [ -d "./terrier/var/results" ];
then
    rm -rf terrier/var/results
fi
mkdir terrier/var/results

# Retrieve
sh terrier/bin/terrier batchretrieve \
	-w BM25 \
	-t parsedFiles/queries \
	-q



echo "\t --> Print defaultResults.txt"

#sh terrier/bin/terrier batchevaluate \
#	-q parsedFiles/qrels

sh terrier/bin/trec_eval.sh \
	-m official \
	parsedFiles/qrels \
	terrier/var/results/BM25_d_3_t_10_0.res \
	> defaultResults.txt