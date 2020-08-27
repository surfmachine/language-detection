# Grundlagen

**Inhaltsverzeichnis**

- [Spracherkennung](#Spracherkennung)  
- [Algorithmen](#Algorithmen)
  - [Wörterbuch](#Wörterbuch)
  - [N-Gramm](#N-Gramm)
- [Weitere Aspekte](#Weitere-Aspekte)
  - [Herausforderungen](#Herausforderungen)
  - [Trefferquote](#Trefferquote)
  - [Zeichensatz](#Zeichensatz)
 
[Zurück zum Hauptmenu](../README.md)


## Spracherkennung
Für Aufgaben wie die Suche im Internet, Indexierung und Auswertung von Dokumenten, Erkennung von Spam Email, Beantwortung von 
Fragen, Verwendung von Chatbots u.v.m. werden sprachabhängige NLP (natural language processing) Modelle eingesetzt. 

Die Basis für den Einsatz solch spezifischer Modelle bildet die korrekte Erkennung der Sprache anhand von Zeichen, Wörtern und Sätzen. 
Dies bezeichnet man als Spracherkennung oder im englischen Language Detection/Identification. Ziel ist die Erreichung einer hohen
Trefferquote. Diese hängt von mehreren Faktoren ab, wie zum Beispiel:
- Länge des Textes
- Art der Wörter und Texte
- Sprachen die unterschieden werden sollen

Bei regulären Texten mit genügend Worten ist mit den heutigen Modellen eine Voraussage mit hoher Präzision sehr gut möglich. 
Schwieriger wird es bei kurzen Texten (wie Tweets, Chats, etc.) oder der Voraussage von sehr nahe verwandten Sprachen (wie Dänisch 
und Norwegisch). 


##  Algorithmen
Für die Intentifikation der Sprache gibt es dabei unterschiedliche Lösungsansätze, unter anderem:
- Ansatz mit Wörterbuch
- N-Gramm Techniken

### Wörterbuch
Bei diesem Ansatz wird die Häufigkeit von Wortformen im Textkorpus untersucht. Das Lexikon enthält dabei Wörter und Wortformen die
sehr häufig in einer Sprache auftreten oder sehr typisch für ein spezifische Sprache sind.

Beispiel sprachspezifische Hinweise:<br />
![Sprachspezifische Hinweise](img/fundamentals-language-hints.png)<br />
Quelle: [Short Text Language Detection with Infinity-Gram](https://de.slideshare.net/shuyo/short-text-language-detection-with-infinitygram-12949447)


> Der Ansatz mit den Wörterbüchern ist einfach, schnell und ausgerichtet auf die Texte welche schon während der Modellerstellung und
Tests verwendet/überprüft wurden. Bei Texten mit seltenem Vokabular sinkt die Erkennungsrate.
> Je nach Einsatzzweck kann das Wörterbuch mit spezifischen Ausdrücken ergänzt werden um die Erkennungsrate zu steigern. Das heisst
für solche Anwendungen steigt die Grösse der Wörterbücher (je Sprache) an. 

### N-Gramm 
Mit der N-Gramm Technik werden Texte in Fragmente zerlegt und jeweils N aufeinanderfolgende Fragmente als N-Gramm zusammengefasst. 
Als Fragmente werden Buchstaben, Phoneme, Wörter, Wendungen oder Ähnliches verwendet. Für die Spracherkennung kommen u.a. Trigramme
zur Anwendung welche als Feature für das Modell (z.B. Naive Bayes Classifier) dienen.  

Beispiel Trigramm:<br />
![](img/fundamentals-trigram.png)<br />
Quelle: [Short Text Language Detection with Infinity-Gram](https://de.slideshare.net/shuyo/short-text-language-detection-with-infinitygram-12949447)

> Das trainierte Modell  kennt die Wahrscheinlichkeiten dieser Trigramme und ermittelt damit (durch Aufsummierung der einzelnen Werte) 
die Textsprache. Die Trefferquote solcher Systeme ist für normale Texte sehr gut. 
> Probleme kann es bei der Unterscheidung von verwandten Sprachen mit identischen oder ähnlichen N-Grammen kommen. 
Eine nachträgliche manuelle Anpassung wie beim Wörterbuch ist kaum möglich.


## Weitere Aspekte

### Herausforderungen
Ist die Sprachidentifikation von Texten noch ein ungelöstes Thema oder sind die existierenden Lösungen ausreichend? 

Wir bereits erwähnt sind Trefferquoten weit über 99% für gut aufgebaute Texte und genügend Wörtern mit den heutigen Lösungen gut
erreichbar. Eine Herausfoderung sind nach wie vor Spezialfälle wie zum Beispiel:
- Kurze Texte (wie zum Beispiel bei Twitter; Tweets sind zu Kurz um Trigramm Features abzuleiten)
- Akronyme, Abkürzungen (wie zum Beispiel LOL für Laughing out loud), seltene Wortformen, etc.
- Texte welche die Rechtschreiberegeln/Orthographie verletzen
- Mehrsprachige Dokumente
- Unterscheidung verwandter Sprachen

### Trefferquote
Je höher die Trefferquote umso besser. Bei 90% hat man immer noch 100 Fehler auf 1'000 Datensätze, daher ist dass in den meisten
Fällen nicht ausreichend. Ein Trefferquoten von 99% und mehr ist daher wünschenswert respektive für viele Anwendungen wichtig.

### Zeichensatz
Je nach Anwendungsfall muss das System auch in der Lage sein, den Zeichensatz zu erkennen, damit die Daten richtig interpretiert 
werden. Dies kann via Metadaten im Dokument selber detektiert werden oder bei Web Services via HTTP Header Informationen. Es gibt
aber immer wieder Fälle bei denen keine oder falsche Angaben vorhanden sind.  

In vielen Anwendungsfällen ist der Zeichensatz aber bekannt, so dass diese "Hürde" wegfällt. 

---
[Zum Seitenanfang](#Grundlagen)  &nbsp; | &nbsp;  [Zum Hauptmenu](../README.md)
