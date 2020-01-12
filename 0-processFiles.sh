#!/bin/bash

# This script transforms malformed doc, queries and qrels files
# located into originalFiles/ directory into files with right format.
#
# It takes in input 3 parameters:
# 	$1 -> file with docs
#	$2 -> file with queries
#	$3 -> file with qrels
# 
# Output of this script is a new directory with the following structure:
#
#	parsedFiles/
#	├── docs
#	├── qrels
#	└── queries

echo "\n\n ------ PARSING FILES ------ \n"

# Clean parsedFiles directory
if [ -d "./parsedFiles" ];
then
	rm -rf parsedFiles
fi
mkdir parsedFiles

# Parse Docs
echo "\t --> Parsing $1"
python parseScript/parseDoc.py $1
mv ${1}Parsed parsedFiles/docs

# Parse Queries
echo "\t --> Parsing $2"
python parseScript/parseQuery.py $2
mv ${2}Parsed parsedFiles/queries

# Parse Qrel
echo "\t --> Parsing $3"
python parseScript/parseQrels.py $3
mv ${3}Parsed parsedFiles/qrels