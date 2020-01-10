
# Set files to index
echo "\n\n ------ SET FILES ------ \n"
sh terrier/bin/trec_setup.sh test

# overwriting current properties with mine
mv terrier/etc/terrier.properties terrier/etc/terrier.properties.bak
cp terrier.properties terrier/etc/terrier.properties

# Removed index dir
if [ -d "./terrier/var/index" ];
then
    rm -rf terrier/var/index
    mkdir terrier/var/index
fi

# indexing of collection
echo "\n\n ------ INDEX CREATION ------ \n"
sh terrier/bin/terrier batchindexing

# Indexing stats
echo "\n\n ------ INDEX STATISTICS ------ \n"
sh terrier/bin/terrier indexstats

# Test it with intecatitive mode
# bin/terrier interactive
