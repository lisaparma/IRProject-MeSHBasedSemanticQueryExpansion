#!/bin/bash

# Parse files
sh 0-processFiles.sh

# Indexing
sh 1-indexing.sh

# Retrival
sh 2-retrival.sh

# Evaluation
echo "\n\n ------ EVALUATION ------ \n"
sh terrier/bin/terrier batchevaluate -q parsedFiles/parsedQrels


echo "\n"