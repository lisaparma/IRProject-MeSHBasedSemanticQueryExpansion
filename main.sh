#!/bin/bash

# Original files
DOCS="originalDocuments/ohsumed.87" 
QUERIES="originalDocuments/query.ohsu.1-63"
QRELS="originalDocuments/qrels.ohsu.batch.87"

if [ ! -d terrier ];
then
    echo " \n --> Terrier not found!"
    echo " Please be sure to have copied into this directory terrier"
    echo " and it has exactly 'terrier' name.\n"
    exit 1
fi

# Parse files
sh 0-processFiles.sh ${DOCS} ${QUERIES} ${QRELS}

# Indexing
sh 1-indexing.sh

# Retrival
sh 2-retrival.sh

# Evaluation
sh 3-evaluation.sh

echo "\n"