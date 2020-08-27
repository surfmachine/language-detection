
import spacy
from spacy_langdetect import LanguageDetector

nlp = spacy.load("en_core_web_sm")

print("------------------------------------------------------------------------")
print("Start LangDetectSpacyDemo")
print("------------------------------------------------------------------------")

nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)
text = "This is English text. Er lebt mit seinen Eltern und seiner Schwester in Berlin. Yo me divierto todos los días en el parque. Je m'appelle Angélica Summer, j'ai 12 ans et je suis canadienne."
doc = nlp(text)

# document level language detection. Think of it like average language of document!
print(doc._.language)

# sentence level language detection
for i, sent in enumerate(doc.sents):
    print(sent, sent._.language)

print("------------------------------------------------------------------------")

text = "War doesn't show who's right, just who's left."
doc = nlp(text)
pred = doc._.language
print(pred, ":", text)

text = "Ein, zwei, drei, vier"
doc = nlp(text)
pred = doc._.language
print(pred, ":", text)

text = "Hello World, this is amazing"
doc = nlp(text)
pred = doc._.language
print(pred, ":", text)

print("------------------------------------------------------------------------")


texts = [
    "Hello World, this is amazing",
    "Hallo Welt, heute ist ein schöner Tag",
    "Bon jour monde, aujourd'hui if fait la Grande Bleue",
    "Guten Tag, how are you?"
]

for text in texts:
    doc = nlp(text)
    pred = doc._.language
    print(pred, ":", text)


