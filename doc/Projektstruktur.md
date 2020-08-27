# Projektstruktur

**Inhaltsverzeichnis**
- [Übersicht](#Übersicht)
- [Data](#Data)
- [Libs](#Libs)
- [Doc](#Doc)
- [Measure](#Measure)
- [Reports](#Reports)
- [Tests](#Tests)
  
[Zurück zum Hauptmenu](../README.md)


## Übersicht
Das Projekt ist wie folgt organisiert:

Verzeichnis           | Inhalt
--------------------- | ------------------------------------------------------------  
[data](../data)       | Testdaten Download, Extraktion und Transformation
[doc](../doc)         | Dokumentation als Markdown
[libs](../libs)       | Spracherkennungs Bibliotheken / Modelle
[measure](../measure) | Klassen für die Messungen der Modelle und das System Monitoring 
[reports](../reports) | Reports und Auswertungen 
[tests](../tests)     | Unit Tests


## Data
In diesem Verzeichnis befinden sich die Scripts für den Download, die Extraktion und Transformation der Testdaten.
Die Daten sind in den folgenden Unterverzeichnissen abgelegt:

Unterverzeichnis               | Inhalt
------------------------------ | ------------------------------------------------------------  
[download](../data/download)   | Rohdaten nach dem Download (sind aus Platzgründen nicht im Repository eingecheckt)
[extract](../data/extract)     | Extrahierte Daten aus den Download Dateien 
[transform](../data/transform) | Transformierte Dateien (im CSV Format) für die Modell- und Performance Tests 

Für den Download, die Extraktion und die Transformation der Daten stehen die folgenden Shell Scritps und Python Klassen
zur Verfügung:

Source Code                                      | Inhalt
------------------------------------------------ | ------------------------------------------------------------  
[download.sh](../data/download.sh)               | Download der WIKI Page Dump Dateien in den Sprachen Deutsch, Französich, Italienisch und Englisch.
[extract.sh](../data/extract.sh)                 | Extraktion der Artikel aus den Wiki Page Dump Dateien.
[transform.py](../data/transform.py)             | Transformation der Artikel der einzelnen Sprachen und Ablage (in verschieden Grössen) als CSV Dateien. 
[transform_mixed.py](../data/transform_mixed.py) | Transformation der Artikel der gemischten Sprachen und Ablage (in verschieden Grössen) als CSV Dateien.
[WikiExtractor.py](../data/WikiExtractor.py)     | Extraktor Klassse von Giuseppe Attardi für die Extraktion der Artikel aus den Wiki Page Dump Dateien.
[WikiTransformer.py](../data/WikiTransformer.py) | Transfomer Klasse für die Transformation der Artikel und das Speichern als CSV.

Die Anlayse der Daten sowie die einzelnen Schritte der Datenverarbeitung werden im Kapitel der [Testdaten](Testdaten.md)
im Detail beschrieben.

## Doc
Das Verzeichnis enthält die Dokumentaion im Markdown Format sowie weitere Bilder und UML Grafiken.

## Libs
Im diesem Verzeichnis befinden sich die Mobiliar internen Bibliotheken sowie die Anbindung der externen Bibliotheken und Cloud 
Dienste. Für jede Bibliothek existiert ein Unterverzeichnis:

Unterverzeichnis                                 | Inhalt
------------------------------------------------ | ------------------------------------------------------------  
[azuretextanalytics](../libs/azuretextanalytics) | Klassen für die Anbindung der Azure Text Analytics Schnittstelle.
[langdetect](../libs/langdetect)                 | Klassen für den Einbindung und Demo der langdetect Bibliothek.
[langdetectspacy](../libs/langdetectspacy)       | Klassen für den Einbindung und Demo der spacy Bibliothek.
[langfromchars](../libs/langfromchars)           | Mobiliar langfromchars Bibliothek und Klassen für die Einbundung und Demo.
[langfromstopwords](../libs/langfromstopwords)   | Mobiliar langfromstopwords Bibliothek und Klassen für die Einbundung und Demo. 
[textblob](../libs/textblob)                     | Klassen für den Einbindung und Demo der textblob Bibliothek.

Zentral sind die folgenden beiden Klassen im `Libs` Verzeichnis:


Source Code                                                                     | Inhalt
------------------------------------------------------------------------------- | ------------------------------------------------------------  
[AbstractLanguageDetectionModel.py](../libs/AbstractLanguageDetectionModel.py)  | Basis Klasse mit einheitlicher Schnittstelle für die Modell- und Performance-Tests. Jede Bibliothek implementiert eine entsprechenden Unterklasse welche die spezifischen Aufrufe der jeweiligen Bibliothek kappselt. 
[ModelFactory.py](../libs/ModelFactory.py)                                      | Factory Klasse für die Instanzierung von Modellen. Je nach Verwendungszweck gibt es diverse `create()` Methoden welche die benötigten Modell Instanzen zurückliefern.

Details zu den Modellen und den Modell Tests sind im Kapitel [Modelle](Modelle.md) ersichtlich. 
Details zu den System Tests im Kapitel [Performance](Performance.md).


## Measure
In diesem Verzeichnis befinden sich die Klassen welche für die verschiedenen Messungen / Tests benötigt werden. 

Modell Tests:

Source Code                                       | Inhalt
------------------------------------------------- | ------------------------------------------------------------  
[ModelMeter.py](../measure/ModelMeter.py)         | Messung der Trefferquote und Zeit. 
[ModelWordMeter.py](../measure/ModelWordMeter.py) | Messung der Trefferquote pro Anzahl Worte. 
[StopWatch.py](../measure/StopWatch.py)           | Messung der Zeit.  
[WordProvider.py](../measure/WordProvider.py)     | Liefert aus einen Text eine Anzahl Wörter.  

Details zu Aufbau, Ausführung und Auswertung der Modell Tests siehe Kapitel [Modelle](Modelle.md).


System/Performance Tests:

Source Code                                                                     | Inhalt
------------------------------------------------------------------ | -------------------------------------------------  
[AbstractSystemMeter.py](../measure/system/AbstractSystemMeter.py) | Basisklasse für die System/Performance Messungen.
[CpuSystemMeter.py](../measure/system/CpuSystemMeter.py)           | Messung der CPU Auslastung.  
[MemorySystemMeter.py](../measure/system/MemorySystemMeter.py)     | Messung des Speicherverbrauch. 
[TimeSystemMeter.py](../measure/system/TimeSystemMeter.py)         | Messung der Geschwindigkeit (Antwortzeit).

Details zu Aufbau, Ausführung und Auswertung der Performance Tests siehe Kapitel [Performance](Performance.md).


## Reports 
Mit Hilfe der Report Klassen werden die Messungen durchgeführt. Als Resultat wird jeweils ein Data Frame zurückgegeben.
Zusätzlich werden alle Resultate als CSV Dateien im Unterverzeichnis `outcome` gespeichert.

Mit Hilfe des Jupiter Notebooks `Visualization` werden die Resultate grafisch ausgewertet. Alle erstellten Grafiken
werden zudem im Unterverzeichnis `graphic` gespeichert. 

Source Code                                                        | Inhalt
------------------------------------------------------------------ | -------------------------------------------------  
[AbstractReport.py](../reports/AbstractReport.py)                  | Basisklasse für alle Reports mit gemeinsamen Methoden.
[ReportDataBalance.py](../reports/ReportDataBalance.py)            | Auswertung wie gut die Daten in den verschiedenen Sprachen ausgeglichen sind.
[ReportScore.py](../reports/ReportScore.py)                        | Auswertung des Score je Modell für Texte in allen 4 Sprachen.
[ReportScorePerLanguage.py](../reports/ReportScorePerLanguage.py)  | Auswertung des Score je Modell und Sprache. 
[ReportScorePerWord.py](../reports/ReportScorePerWord.py)          | Auswertung des Score je Modell und Anzahl Wörter für Texte in allen 4 Sprachen. 
[ReportScoreProbability.py](../reports/ReportScoreProbability.py)  | Auswertung Wahrscheinlichkeit des Score je Modell für Texte in allen 4 Sprachen. 
[ReportSystemPerformance.py](../reports/ReportSystemPerformance.py)| Auswertung Zeit, CPU Belastung und Speicherverbrauch je Modell.
[Visualization.ipynb](../reports/Visualization.ipynb)              | Visualisierung aller Auswertungsresultate.

Details zu den Auswertungen der Modell Tests siehe Kapitel [Modelle](Modelle.md). 
Details zu den Auswertungen der Performance Tests siehe Kapitel [Performance](Performance.md). 

## Tests
Im Verzeichnis Tests befinden sich rund 10 Unittests zu einzelnen Python Klassen wie zum Beispiel dem 
`WikiTransformer` oder der `StopWatch`. Die Testklassen heissen entsprechend `WikiTransformerTest` respektive 
`StopWatchTest`. Zudem hat es Testdaten Sets mit kleinen Datenmengen oder spezifischen Datenkonstelationen. 
Damit wird eine schnelle Ausführung der Tests möglich oder es können spezifische Bereinigungen und Transformation der
Daten simuliert und überprüft werden.

Es sich gezeigt dass mit diesem Ansatz sehr effektive Python Code entwickelt und mit dem Debugger analysiert werden kann.
Zudem hat man ein Set von Tests die jederzeit wiederholt werden können, ohne das eine Visuelle Kontrolle notwendig ist, 
wie das beim Arbeiten mit Jupiter Notebooks der Fall ist.

---
[Zum Seitenanfang](#Projektstruktur)  &nbsp; | &nbsp;  [Zum Hauptmenu](../README.md)
