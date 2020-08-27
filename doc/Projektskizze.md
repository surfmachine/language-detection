# Projektskizze 
Berner Fachhochschule BFH - CAS Practical Machine Learning - Semesterarbeit - Language Detection

**Inhaltsverzeichnis**
- [Ausgangslage](#Ausgangslage)
- [Problemstellung](#Problemstellung)
- [Lösungsansatz](#Lösungsansatz)
- [Personen](#Personen)

[Zurück zum Hauptmenu](../README.md)

## Ausgangslage
Die Mobiliar hat diverse Machine Learning Modelle für die Unterstützung von Geschäftsprozessen produktiv im Einsatz. 
Weitere Anwendungsmöglichkeiten werden von Data Scientists laufend untersucht und mit den Fachverantwortlichen verprobt. 

Neben der Entwicklung neuer Modelle ist auch das  Engineering und der professionelle Betrieb (in Anlehnung an «DevOps» 
häufig als «MLOps» bezeichnet) ein wichtiger Aspekt. Hierzu existiert in der Mobiliar ein interdisziplinäres Team von 
Data Scientists und Software Engineers. 

Aktuell besteht Ihre Aufgabe in der Erarbeitung und Bereitstellung eines «Data Science Workplace» in der Cloud, sowie 
die Evaluation von Services, Frameworks und Tools im Bereich Machine Learning. 

Als «preferred Cloud Provider» setzt die Mobiliar Microsoft Azure ein. Dort werden unter dem Begriff **Azure Cognitive 
Services** eine Reihe von interessanten Diensten im Bereich Bild, Sprache und Text zur Verfügung gestellt, welche 
Microsoft zum Teil auch in den eigenen Produkten einsetzt.


##	Problemstellung
Im Rahmen dieser Semesterarbeit sollen die Möglichkeiten der Text Analytics Dienste der Azure Cognitive Services 
erkundet werden. Die Text Analytics Dienste bieten Funktionen zur Spracherkennung, Extraktion von Schlüsselbegriffen und 
Entitäten sowie eine Funktion zur Sentiment Analyse an.

Aufgabe ist es, die Spracherkennung im Detail zu prüfen und mit den beiden Mobiliar internen Bibliotheken 
(langfromstopwords und langfromchars) als auch der öffentlichen Bibliothek lang-detect(2) zu vergleichen. 
Unter Spracherkennung ist in diesem Kontext gemeint, in welcher Sprache (Deutsch, Französisch, etc.) der untersuchte 
Text verfasst wurde.

Hierzu soll ein einfacher Prototype mit Python erstellt werden, welche die genannten Modelle überprüft. Neben der 
Prognose Genauigkeit sollen dabei auch Aussagen zur Geschwindigkeit, Speicherverbrauch, Kosten und Einfachheit der 
Einbindung gemacht werden.

Hintergrund:
Für den mehrsprachigen Schweizermarkt ist die Spracherkennung für die Mobiliar eine wichtige Funktion. Sie kommt für die 
automatische Triage von Mails oder bei Live Chatbots zur Anwendung. Ein weiteres Anwendungsgebiet ist der Einsatz von 
unterschiedlichen Klassifikationsmodellen je nach Sprache. 

Für Realtime Anwendungen wie Chatbots sollen die Modelle möglichst wenig Speicher belegen und schnell sein. Die Modelle 
sollen auch bei Anwendungsfällen mit wenig Text möglichst gut performen und mit der «Versicherungssprache» der Mobiliar 
und deren Kunden klarkommen.


## Lösungsansatz
Der Lösungsansatz besteht aus folgenden Teilaufgaben:

1. Wissensaufbau betreffend den verschieden Ansätzen zur Spracherkennung, den zu prüfenden Bibliotheken und der Text 
   Analytics Schnittstelle von Azure.

2. Erstellung Prototyp für den Aufruf der Text Analytics Schnittstelle und den anderen Bibliotheken.

3. Bereitstellung und Bereinigung von Testdaten.

4. Prototyp soweit ausbauen, dass die Tests automatisiert ausgeführt werden können.

5. Durchführung Tests und Protokollierung der Messdaten.

6. Auswertung der Testergebnisse (Modelle vergleichen) und Fertigstellung Bericht.


## Personen
Studierender:<br />	
Die Mobiliar, Thomas Iten

Ansprechpartner / Betreuer in der Firma:<br />	
Die Mobiliar, Marcus Schwemmle

Experte:<br />
BFH, Max Kleiner

---
[Zum Seitenanfang](#Projektskizze)  &nbsp; | &nbsp;  [Zum Hauptmenu](../README.md)
