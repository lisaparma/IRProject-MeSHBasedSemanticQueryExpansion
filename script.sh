#!/bin/bash

DOCS="ohsumed.87" 
QUERIES="query.ohsu.1-63"

# Parse files
echo "\n\n ------ PARSE FILES ------ \n"
if [ -d "./parsedFiles" ];
then
	rm -rf parsedFiles
fi
mkdir parsedFiles

# Parse Docs and Queries
echo "\t --> Parsing ${DOCS} and moving it to parsedFiles/parsedDocs"
python parseScript/parseDoc.py originalDocuments/${DOCS}
mv originalDocuments/${DOCS}Parsed parsedFiles/parsedDocs

echo "\t --> Parsing ${QUERIES} and moving it to parsedFiles/parsedQueries"
python parseScript/parseQuery.py originalDocuments/${QUERIES}
mv originalDocuments/${QUERIES}Parsed parsedFiles/parsedQueries


# Set files to index
echo "\n\n ------ SET FILES ------ \n"
sh terrier/bin/trec_setup.sh parsedFiles/parsedDocs


# Overwriting current properties with mine
mv terrier/etc/terrier.properties terrier/etc/terrier.properties.bak
cp terrier.properties terrier/etc/terrier.properties

# Remove index dir and create a new one
if [ -d "./terrier/var/index" ];
then
    rm -rf terrier/var/index
    mkdir terrier/var/index
else 
	mkdir terrier/var/index
fi

# Indexing of collection
echo "\n\n ------ INDEX CREATION ------ \n"
sh terrier/bin/terrier batchindexing

# Indexing stats
echo "\n\n ------ INDEX STATISTICS ------ \n"
sh terrier/bin/terrier indexstats

# Indexing stats
echo "\n\n ------ RETRIVAL ------ \n"
sh terrier/bin/terrier batchretrieve \
	-w BM25 \
	-t parsedFiles/parsedQueries


# TODO
#echo "\n\n ------ EVALUATE ------ \n"
#sh terrier/bin/terrier batchevaluate -q qrels.ohsu.batch.87


echo "\n"