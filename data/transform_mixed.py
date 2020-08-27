import os
from pathlib import Path
from WikiTransformer import WikiTransformer

#
# create a mixed csv file for a given list of languages and a total number of articles
#
def create_articles(language, wiki_base, wiki_files, number_of_articles):
    wikiTransformer = WikiTransformer(max_articles=number_of_articles)
    for wiki_file in wiki_files:
        wiki_path = wiki_base + "/" + language

        docs = wikiTransformer.read_file(wiki_path, wiki_file)
        wikiTransformer.transform(language, docs)

        if (wikiTransformer.max_articles_reached()):
            break

    return wikiTransformer.articles


def create_mixed_csv(languages, wiki_base, wiki_files, number_of_articles_per_language):
    language_articles = []
    for language in languages:
        articles = create_articles(language, wiki_base, wiki_files, number_of_articles_per_language)
        language_articles.append(articles)

    articles = []
    for n in range(number_of_articles_per_language):
        for i in range(len(languages)):
            articles.append(language_articles[i][n])

    return articles

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
# Create mixed csv files
#
for size in sizes:
    number_of_articles = int(size * 1000 / len(languages))
    csv_file = csv_file_prefix + "_all_" + str(size) + "k.csv"
    fn = Path(csv_path)/csv_file
    if os.path.exists(fn):
        print("Create {0} skipped, file already exists".format(csv_file))
    else:
        print("Create {0}".format(csv_file))
        articles = create_mixed_csv(languages, wiki_base, wiki_files, number_of_articles)
        wikiTransformer = WikiTransformer()
        wikiTransformer.articles = articles
        wikiTransformer.write_csv(csv_path, csv_file)
