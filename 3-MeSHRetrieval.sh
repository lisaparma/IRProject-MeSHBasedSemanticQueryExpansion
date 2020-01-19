#!/bin/bash

# This script perform retrieval & evaluation of "parsedFiles/queries"

echo "\n\n ------ QUERY EXPANSION RETRIEVAL ------ \n"

# Perform query expansion
echo "\t --> Query expansion of $1"
python3 parseScript/QEScript.py $1
mv ${1}QueryExpansion parsedFiles/expandedQueries

# Clean results directory
if [ -d "./terrier/var/results" ];
then
    rm -rf terrier/var/results
fi
mkdir terrier/var/results

# Retrieve
sh terrier/bin/terrier batchretrieve \
	-w BM25 \
	-t parsedFiles/expandedQueries \
	-q

echo "\t --> Print queryExpansionResults.txt"

#sh terrier/bin/terrier batchevaluate \
#	-q parsedFiles/qrels

sh terrier/bin/trec_eval.sh \
	-m official \
	parsedFiles/qrels \
	terrier/var/results/BM25_d_3_t_10_0.res \
	> results/queryExpansionResults.txt