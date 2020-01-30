#!/bin/bash

# This script perform retrieval & evaluation of "parsedFiles/queries"

echo "\n\n ------ QUERY EXPANSION RETRIEVAL ------ \n"

# Perform query expansion
echo "\t --> Query expansion of $1"
python3 queryExpansionScript/QueryExpansionScript.py $1
mv QueriesExp-run2 parsedFiles/queriesExp-run2
mv QueriesExp-run3 parsedFiles/queriesExp-run3
mv QueriesExp-run4 parsedFiles/queriesExp-run4
mv QueriesExp-run5 parsedFiles/queriesExp-run5

# RUN 2
sh terrier/bin/terrier batchretrieve \
	-w BM25 \
	-t parsedFiles/queriesExp-run2 \
	-Dtrec.results.file=bm25_run2.res

sh terrier/bin/trec_eval.sh \
	-m official \
	parsedFiles/qrels \
	terrier/var/results/bm25_run2.res \
	> results/QErun2-results.txt
echo "\t --> Printed QErun2-results.txt"


# RUN 3
sh terrier/bin/terrier batchretrieve \
	-w BM25 \
	-t parsedFiles/queriesExp-run3 \
	-Dtrec.results.file=bm25_run3.res

sh terrier/bin/trec_eval.sh \
	-m official \
	parsedFiles/qrels \
	terrier/var/results/bm25_run3.res \
	> results/QErun3-results.txt

echo "\t --> Printed QErun3-results.txt"


# RUN 4
sh terrier/bin/terrier batchretrieve \
	-w BM25 \
	-t parsedFiles/queriesExp-run4 \
	-Dtrec.results.file=bm25_run4.res

sh terrier/bin/trec_eval.sh \
    -m official \
	parsedFiles/qrels \
	terrier/var/results/bm25_run4.res \
	> results/QErun4-results.txt

echo "\t --> Printed QErun4-results.txt"


# RUN 5
sh terrier/bin/terrier batchretrieve \
	-w BM25 \
	-t parsedFiles/queriesExp-run5 \
	-Dtrec.results.file=bm25_run5.res

sh terrier/bin/trec_eval.sh \
	-m official \
	parsedFiles/qrels \
	terrier/var/results/bm25_run5.res \
	> results/QErun5-results.txt

echo "\t --> Printed QErun5-results.txt"