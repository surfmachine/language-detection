# Language Detection 
Semesterarbeit CAS **Practical Machine Learning** der Berner Fachhochschule BFH. <br />
Q3/2020, Thomas Iten

## Inhalt
- Projektorganisation
  - [Projektskizze](doc/Projektskizze.md)
  - [Planung und Arbeitsrapporte](doc/Planung.md)
- Projektaufbau
  - [Installation](doc/Installation.md) 
  - [Projektstrukur](doc/Projektstruktur.md)
- Projektarbeiten  
  - [Grundlagen](doc/Grundlagen.md) 
  - [Testdaten](doc/Testdaten.md) 
  - [Modelle](doc/Modelle.md)
  - [Performance](doc/Performance.md) 
- [Ergebnisse](doc/Ergebnisse.md)
- [Referenzen](doc/Referenzen.md)


## Management Summary

### Ausgangslage
Für den mehrsprachigen Schweizermarkt ist die Spracherkennung für die Mobiliar eine wichtige Funktion. Sie kommt für die 
automatische Triage von Mails oder bei Live Chatbots zur Anwendung. Ein weiteres Anwendungsgebiet ist der Einsatz von 
unterschiedlichen Klassifikationsmodellen je nach Sprache. Für Realtime Anwendungen wie Chatbots sollen die Modelle 
möglichst wenig Speicher belegen und schnell sein. 

In Zukunft wird die Mobiliar einen Grossteil Ihrer Anwendungen in der Cloud betreiben. Als «preferred Cloud Provider» 
setzt die Mobiliar dabei auf Microsoft Azure. Azure bietet umfangreiche Cognitive Services an, welche in den Microsoft 
eigenen Produkten zum Einsatz kommen. 

### Zielsetzung
Im Rahmen dieser Semesterarbeit sollen die Möglichkeiten der Text Analytics Dienste der Azure Cognitive Services 
erkundet werden. Die Text Analytics Dienste bieten Funktionen zur Spracherkennung, Extraktion von Schlüsselbegriffen 
und Entitäten sowie eine Funktion zur Sentiment Analyse an.

Aufgabe ist es, die Spracherkennung im Detail zu prüfen und mit den beiden Mobiliar internen Bibliotheken 
LangFromStopwords und LangFromChars als auch der öffentlichen Bibliothek LangDetect zu vergleichen. Auf Wunsch des Experten 
wurden mit LangDetectSpacy und TextBlob zwei weitere öffentliche  Bibliotheken der Untersuchung hinzugefügt. 
Unter Spracherkennung ist in diesem Kontext gemeint, in welcher Sprache (Deutsch, Französisch, Italienisch oder  Englisch) 
der untersuchte Text verfasst wurde. 

### Ergebnisse
Die Trefferquote für grosse Texte ist bei allen geprüften Bibliotheken gut bis ausgezeichnet. Anstelle der Mobiliar 
internen Bibliotheken LangFromStopwords und LangFromChars gibt es mit LangDetect und Spacy zwei sehr gute, kostenlose 
Alternativen welche in den Tests besser abgeschnitten haben.

Wenn es Einschränkungen bei den Ressourcen (Zeit, Memory, CPU) gibt ist allenfalls die LangFromStopwords Bibliothek eine 
interessante Variante. Ausserdem kann das Modell durch anpassen der Wortlisten einfacher auf spezifisches Vokabular 
ausgerichtet werden als die anderen Lösungen. Für den Einsatz mit Italienisch müsste die aktuelle Lösung allerdings 
verbessert werden.

Der kostenpflichtige Text Analytics Service schneidet insgesamt am besten ab. Dies ist vor allen bei der Spracherkennung 
mit wenig Text auffällig. Hier erreicht der Service die mit Abstand besten Werte. 

