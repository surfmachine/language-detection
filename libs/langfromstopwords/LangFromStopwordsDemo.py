
from mobi.LangFromStopwords import LangFromStopwords

model = LangFromStopwords();

print("------------------------------------------------------------------------")
print("Start LangFromStopwordsDemo")
print("------------------------------------------------------------------------")

text = "Hello World, this is amazing"
pred = model.predict_single(text)
print(pred, ":", text)


texts = [
    "Hello World",
    "Hallo Welt",
    "Bon jour monde",
    "Guten Tag, how are you?",
    "Sarebbe troppo bello per essere vero",
    "LOL"
]
for text in texts:
    pred = model.predict_single(text, True)
    print(pred, ":", text)


pred = model.predict(texts, True)
print(pred)
