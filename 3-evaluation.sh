#!/bin/bash

# This script perform evluation

echo "\n\n ------ EVALUATION ------ \n"

sh terrier/bin/terrier batchevaluate \
	-q parsedFiles/qrels