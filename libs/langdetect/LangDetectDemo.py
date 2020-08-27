
from langdetect import detect
from langdetect import detect_langs

print("------------------------------------------------------------------------")
print("Start LangDetectDemo")
print("------------------------------------------------------------------------")

text = "War doesn't show who's right, just who's left."
pred = detect(text)
print(pred, ":", text)

text = "Ein, zwei, drei, vier"
pred = detect(text)
print(pred, ":", text)

text = "Hello World, this is amazing"
pred = detect_langs(text)
print(pred, ":", text)

texts = [
    "Hello World, this is amazing",
    "Hallo Welt, heute ist ein schöner Tag",
    "Bon jour monde, aujourd'hui if fait la Grande Bleue",
    "Guten Tag, how are you?"
]
for text in texts:
    pred = detect_langs(text)
    print(pred, ":", text)


