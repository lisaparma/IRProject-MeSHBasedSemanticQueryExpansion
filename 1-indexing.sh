#!/bin/bash

# This script set:
#	- docs to parse (parsedFiles/docs),
# 	- settings to use (terrier.properties)
#
# It also performs indexing returning some helpfull statistics.

echo "\n\n ------ SET FILES ------ \n"

# Setting of docs
sh terrier/bin/trec_setup.sh parsedFiles/docs

# Overwriting current properties with mine
mv terrier/etc/terrier.properties terrier/etc/terrier.properties.bak
cp terrier.properties terrier/etc/terrier.properties


# Indexing of collection
echo "\n\n ------ INDEX CREATION ------ \n"

# Clean index directory
if [ -d "./terrier/var/index" ];
then
    rm -rf terrier/var/index
fi
mkdir terrier/var/index

# Perform indexing
sh terrier/bin/terrier batchindexing


# Index stats
echo "\n\n ------ INDEX STATISTICS ------ \n"
sh terrier/bin/terrier indexstats