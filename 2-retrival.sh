#!/bin/bash

echo "\n\n ------ RETRIVAL ------ \n"
# Remove results dir and create a new one
if [ -d "./terrier/var/results" ];
then
    rm -rf terrier/var/results
    mkdir terrier/var/results
else 
	mkdir terrier/var/results
fi

sh terrier/bin/terrier batchretrieve \
	-w BM25 \
	-t parsedFiles/parsedQueries
