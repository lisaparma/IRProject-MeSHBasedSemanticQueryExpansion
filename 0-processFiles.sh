#!/bin/bash

DOCS="ohsumed.87" 
QUERIES="query.ohsu.1-63"
QRELS="qrels.ohsu.batch.87"

# Parse files
echo "\n\n ------ PARSE FILES ------ \n"
if [ -d "./parsedFiles" ];
then
	rm -rf parsedFiles
fi
mkdir parsedFiles

# Parse Docs, Queries and Qrels
echo "\t --> Parsing ${DOCS} and moving it to parsedFiles/parsedDocs"
python parseScript/parseDoc.py originalDocuments/${DOCS}
mv originalDocuments/${DOCS}Parsed parsedFiles/parsedDocs

echo "\t --> Parsing ${QUERIES} and moving it to parsedFiles/parsedQueries"
python parseScript/parseQuery.py originalDocuments/${QUERIES}
mv originalDocuments/${QUERIES}Parsed parsedFiles/parsedQueries

echo "\t --> Parsing ${QRELS} and moving it to parsedFiles/parsedQrels"
python parseScript/parseQrels.py originalDocuments/${QRELS}
mv originalDocuments/${QRELS}Parsed parsedFiles/parsedQrels