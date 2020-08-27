#!/usr/bin/env bash

# -------------------------------------------------------------------------------------------------
# Get wiki article text dumps for the languages de, fr, it and en.
#
# The wiki dump files can be downloaded from wikimedia. Details see: https://dumps.wikimedia.org.
#
# Note:
# - The downloaded dump files are between 3 and 17GB and therefor not part of the project.
# - To download the dumps use the download.sh script or just a browser.
# -------------------------------------------------------------------------------------------------

echo "Download start..."
date

# italian
wget -c https://dumps.wikimedia.org/itwiki/latest/itwiki-latest-pages-articles.xml.bz2

# french
wget -c https://dumps.wikimedia.org/frwiki/latest/frwiki-latest-pages-articles.xml.bz2

# german
wget -c https://dumps.wikimedia.org/dewiki/latest/dewiki-latest-pages-articles.xml.bz2

# english
wget -c https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2

echo "Download finished."
date

# Wait to continue
read -p "\nPress enter to finish..."