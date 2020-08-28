# Planung und Arbeitsrapporte

**Inhaltsverzeichnis**
- [Aufgabe](#Aufgabe)
  - [Problemstellung](#Problemstellung)
  - [Lösungsansatz](#Lösungsansatz)
- [Planung](#Planung)
- [Arbeitsrapporte](#Arbeitsrapporte)
  
[Zurück zum Hauptmenu](../README.md)


## Aufgabe

### Problemstellung
Im Rahmen dieser Semesterarbeit sollen die Möglichkeiten der Text Analytics Dienste der Azure Cognitive Services erkundet werden. 
Die Text Analytics Dienste bieten Funktionen zur Spracherkennung, Extraktion von Schlüsselbegriffen und Entitäten sowie eine 
Funktion zur Sentiment Analyse an. 

Aufgabe ist es, die Spracherkennung im Detail zu prüfen und mit den beiden Mobiliar internen Bibliotheken (langfromstopwords und 
langfromchars) als auch der öffentlichen Bibliothek lang-detect zu vergleichen. Unter Spracherkennung ist in diesem Kontext gemeint, 
in welcher Sprache (Deutsch, Französisch, etc.) der untersuchte Text verfasst wurde. 

Hierzu soll ein einfacher Prototype mit Python erstellt werden, welche die genannten Modelle überprüft. Neben der Prognose 
Genauigkeit sollen dabei auch Aussagen zur Geschwindigkeit, Speicherverbrauch, Kosten und Einfachheit der Einbindung gemacht werden.

### Lösungsansatz
Der Lösungsansatz besteht aus folgenden Teilaufgaben:

1.	Wissensaufbau betreffend den verschieden Ansätzen zur Spracherkennung, den zu prüfenden Bibliotheken und der 
    Text Analytics Schnittstelle von Azure.
2.	Erstellung Prototypen für den Aufruf der Text Analytics Schnittstelle und den anderen Bibliotheken.
3.	Bereitstellung und Bereinigung von Testdaten.
4.	Prototyp soweit ausbauen, dass die Tests automatisiert ausgeführt werden können.
5.	Durchführung Tests und Protokollierung der Messdaten.
6.	Auswertung der Testergebnisse (Modelle vergleichen) und Fertigstellung Bericht.


## Planung 

 Nr. | Arbeitsschritte                                       | Datum      | Status
---- | ----------------------------------------------------- | ---------- | ----------
 1.0 | Know How Spracherkennung und Azure Text Analytics     | 12.08.2020 | Erledigt
 2.0 | Prototyp Libraries                                    | 14.07.2020 | Erledigt
 2.1 | Prototyp Text Analytics Schnittstelle                 | 18.08.2020 | Erledigt
 3.0 | Bereitstellung und Bereinigung  Testdaten             | 15.07.2020 | Erledigt  
 4.0 | Generisches Modell API erstellen und prüfen           | 17.07.2020 | Erledigt
 4.1 | Metriken Score/Probability definieren und prüfen      | 28.07.2020 | Erledigt
 4.2 | Metriken Ressourcen/Performance definieren und prüfen | 31.07.2020 | Erledigt
 n/a | Experten Meeting an der BFH                           | 14.08.2020 | Erledigt
 5.0 | Durchführung und Protokollierung Messdaten            | 24.08.2020 | Erledigt
 6.1 | Auswertung der Testergebnisse (Modelle vergleichen)   | 24.08.2020 | Erledigt
 6.2 | Projektdokumentation mittels Markdown                 | 24.08.2020 | In Arbeit
 6.3 | Fertigstellung Bericht & Projekt, Abgabe an Experte   | 31.08.2020 | ...
 6.4 | Präsentation erstellen                                | 06.09.2020 | ...
 6.5 | Präsentation und Abgabe Bericht                       | 15.09.2020 | ...


## Arbeitsrapporte

 Datum     | Aufwand | Arbeit
---------- | ------- | ---------------------------------------------------------------
08.07.2020 |  2.00h  | Einbindung Mobiliar LangFromStopwords, Erstellung LangFromStopwordsDemo
09.07.2020 |  6.00h  | Einbindung Mobiliar LangFromChars mit abhängigen Libraries, Erstellung ConsoleLogger und LangFromCharsDemo
10.07.2020 |  1.00h  | Einbindung langdetect, Erstellung LangDetectDemo
10.07.2020 |  3.00h  | Einbindung spacy, Fehlersuche und Behebunbg SSLCertVerificationError bei Installation, Erstellung LangDetectSpacyError  
11.07.2020 |  2.50h  | Suche Testdaten und Download Wiki Artikel Dumps, Erstellung download.sh 
12.07.2020 |  3.00h  | Extraktion Artikel Texte aus Wiki Artikle Dumps, Erstellung extract.sh
13.07.2020 |  9.00h  | Daten Transformation mit WikiTranformer und WikiTransformerTest  
14.07.2020 |  8.00h  | Daten Transformation mit WikiTranformer und WikiTransformerTest, transform und transform_mixed  
15.07.2020 |  7.00h  | Strukturierung Dokumentation und Beschreibung Installation und Testdaten Aufbereitung.    
15.07.2020 |  1.00h  | Einbindung textblob, Erstellung TextBlobDemo    
15.07.2020 |  2.50h  | Erstellung AbstractPrediction API mit LangFromCharsPrediction und PredictionTest    
16.07.2020 |  9.00h  | Anpassen AbstractPrediction auf AbstractLanguageDetectionModel, Erstellung Modell Implementation und LanguageDetectionModelTest 
17.07.2020 |  3.50h  | Fehlersuche Artikel Text mit NAN, Erstellung Testfall test_article_nan, Anpassung WikiTransformer. Erstellung WikiTransfomerNaNTest
17.07.2020 |  3.50h  | Erstellung StopWatch und ReportScoreTest zum schnellen Testen des Score und der Modell API
19.07.2020 |  2.00h  | Refactoring Modell Implementationen, Erstellung Facotry, Integration TextBlob Library 
21.07.2020 |  2.00h  | Erstellung ReportScorePerLanguageTest
22.07.2020 |  2.00h  | Erstellung ModelMeter, Refactoring Tests and ModelFactory
23.07.2020 |  1.50h  | Erstellung ReportDataBalanceTest und Dokumentation Testdaten Balance
24.07.2020 |  3.50h  | Erstellung WordProvider und WordProviderTest, ReportScorePerWordTest
25.07.2020 |  2.00h  | Erstellung ModelWordMeter und ModelWordMeterTest, Refactoring ReportScorePerWordTest
26.07.2020 |  3.00h  | Erweiterung ModelMeter, Erstellung ModelMeterTest und ReportScoreProbabilityTest 
26.07.2020 |  3.00h  | Refactoring Reports in eigenes Verzeichnis, Anpassung df Strukturen und Ausgabe
27.07.2020 |  2.50h  | Recherche Python System Monitoring Tools, PsUtilDemo, ResourceDemo, TracemallocDemo
28.07.2020 |  2.00h  | CPU Messung eingebaut bei PsUtilDemo, ModuleNotFoundError behoben bei start mit shell
29.07.2020 |  3.00h  | Erstellung Abstract SystemMeter, CpuSystemMeter, MemorySystemMeter, TimeSystemMeter und SystemMeterTest
29.07.2020 |  1.50h  | Erstellung ReportSystemPerformance und erste Tests
09.08.2020 |  3.00h  | Markdown Dokumentation Performance (Kapitel Bibliotheken, Messungen und Ressourcen)
11.08.2020 |  3.00h  | Markdown Dokumentation Grundlagen, First Draft
12.08.2020 |  4.00h  | Markdown Dokumentation Grundlagen, Erste Version erstellt
13.08.2020 |  9.00h  | Markdown Dokumentation Organisation Markdown Struktur, Modelle, Planung, Projekskizze ujdn Projektstruktur
14.08.2020 |  6.00h  | Besprechung mit Experte, Erstellung Azure Cognitive Service Account und erstes AzureTextAnalyticsDemo 
15.08.2020 |  4.00h  | Erstellung AzureDataHandler, AzureDataHandlerTest, AzureTextAnalyticsModel und AzureTextAnalyticsModelTest
15.08.2020 |  4.50h  | Erstellung AbstractReport, Anpassung aller Reports und Ausführung aller Reports
18.08.2020 | 10.00h  | Visualisierung ReportScore, ReportScorePerLanguage, ReportScorePerWord, ReportSystemPerformance
19.08.2020 |  1.50h  | Visualisierung speichern als Image (PNG)
20.08.2020 |  7.00h  | Visualisierungen Wahrscheinlichkeiten mit Bar-, Line und Boxplots 
21.08.2020 |  2.00h  | Markdown Dokumentation Fertigstellung Installation
22.08.2020 |  4.00h  | Markdown Dokumentation Modelle Langdetect, Spacy, Azure, Auswertungen Modelle und Performance, Navigation Seiten 
24.08.2020 |  3.00h  | Markdown Installation und Projekstruktur fertig gestellt. 
25.08.2020 |  1.50h  | Markdown Testdaten fertig gestellt und Modelle angefangen 
26.08.2020 |  3.00h  | Markdown Modelle und Performance fertig gestellt
Total      |154.50h  | Aufwand

---
[Zum Seitenanfang](#Planung-und-Arbeitsrapporte)  &nbsp; | &nbsp;  [Zum Hauptmenu](../README.md)
