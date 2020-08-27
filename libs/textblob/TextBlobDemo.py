from textblob import TextBlob

print("------------------------------------------------------------------------")
print("Start TextBlobDemo")
print("------------------------------------------------------------------------")

text = "War doesn't show who's right, just who's left."
blob = TextBlob(text)
pred = blob.detect_language()
print(pred, ":", text)

