#!/bin/bash

echo "\n --> TREC9-TRAIN "
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

# Retrival and evaluation of default Queries
sh 2-defaultRetrieval.sh

# Retrieval and evaluation of expanded queries
sh 3-MeSHRetrieval.sh parsedFiles/queries