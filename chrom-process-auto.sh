#!/bin/bash

chrom=$1

wget ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606/chr_rpts/chr_$chrom.txt.gz

zcat chr_$chrom.txt.gz | awk '/^[0-9]/{print "rs"$1}' > chr$chrom.rsIDs

sed -i '1i#rsid' chr$chrom.rsIDs

rm chr_$chrom.txt.gz


