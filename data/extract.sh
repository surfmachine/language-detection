#!/usr/bin/env bash

# -------------------------------------------------------------------------------------------------
# Extract article texts from Wiki page dumps.
#
# For the extration of the article texts from the wiki dump files, the WikiExtractor
# form Giuseppe Attardi is used. Further details see: https://github.com/attardi/wikiextractor
# -------------------------------------------------------------------------------------------------

echo "Extratcting start..."
date

# italian
python WikiExtractor.py --processes 4 --min_text_length 20 -b 100M --no_templates --filter_disambig_pages -q -o extract dump/itwiki-latest-pages-articles.xml.bz2
mv extract/AA extract/it

# french
python WikiExtractor.py --processes 4 --min_text_length 20 -b 100M --no_templates --filter_disambig_pages -q -o extract dump/frwiki-latest-pages-articles.xml.bz2
mv extract/AA extract/fr

# german
python WikiExtractor.py --processes 4 --min_text_length 20 -b 100M --no_templates --filter_disambig_pages -q -o extract dump/dewiki-latest-pages-articles.xml.bz2
mv extract/AA extract/de

# english
python WikiExtractor.py --processes 4 --min_text_length 20 -b 100M --no_templates --filter_disambig_pages -q -o extract dump/enwiki-latest-pages-articles.xml.bz2
mv extract/AA extract/en

echo "Extratcting finished."
date

# Wait to continue
read -p "\nPress enter to finish..."