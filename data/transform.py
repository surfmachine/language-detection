import os
from pathlib import Path
from WikiTransformer import WikiTransformer

#
# create a csv file for a given language and number of articles
#
def create_csv(language, wiki_base, wiki_files, number_of_articles, csv_base, csv_file):
    wikiTransformer = WikiTransformer(max_articles=number_of_articles)
    # transform articles
    for wiki_file in wiki_files:
        wiki_path = wiki_base + "/" + language

        docs = wikiTransformer.read_file(wiki_path, wiki_file)
        wikiTransformer.transform(language, docs)

        if (wikiTransformer.max_articles_reached()):
            break
    # write csv file
    wikiTransformer.write_csv(csv_base, csv_file)

#
# Init
#
wiki_base  = "extract"                  # Base directory of wiki files
wiki_files = []                         # List of Wiki files ['wiki_00', .. 'wiki_12']
for i in range(0, 13):
    wiki_files.append( "wiki_" + str(i).zfill(2) )

csv_path  = "transform"                 # Target directory of generated CSV files
csv_file_prefix = "articles"            # Prefix of the csv files

languages = ['de', 'en', 'fr', 'it']    # languages of the test data
sizes = [1, 5, 10, 100]                 # Number of articles per csv file in kilo

#
# Create csv files per language
#
for language in languages:
    for size in sizes:
        number_of_articles = size * 1000
        csv_file = csv_file_prefix + "_" + language + "_" + str(size) + "k.csv"
        fn = Path(csv_path)/csv_file
        if os.path.exists(fn):
            print("Create {0} skipped, file already exists".format(csv_file))
        else:
            print("Create {0}".format(csv_file))
            create_csv(language, wiki_base, wiki_files, number_of_articles, csv_path, csv_file)
