#!/bin/bash

# This script perform evluation

echo "\n\n ------ EVALUATION ------ \n"

sh terrier/bin/terrier batchevaluate \
	-q parsedFiles/qrels


#sh terrier/bin/trec_eval.sh \
#	-m official \
#	parsedFiles/qrels \
#	terrier/var/results/BM25_d_3_t_10_0.res \
#	> results.txt