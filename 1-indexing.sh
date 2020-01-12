#!/bin/bash

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