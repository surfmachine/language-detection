
from mobi.LangFromChars import LangFromChars
model = LangFromChars();

print("------------------------------------------------------------------------")
print("Start LangFromCharsDemo")
print("------------------------------------------------------------------------")

text = "Hello World, this is amazing"
pred = model.predict(text)
print(pred, ":", text)


texts = [
    "Hello World, this is amazing",
    "Hallo Welt, heute ist ein schöner Tag",
    "Bon jour monde, aujourd'hui if fait la Grande Bleue",
    "Guten Tag, how are you?"
]
for text in texts:
    pred = model.predict_language_with_propa(text)
    print(pred, ":", text)


