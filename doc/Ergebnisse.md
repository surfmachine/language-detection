# Ergebnisse

**Inhaltsverzeichnis**
- [Modell Messungen](#Modell-Messungen)
- [Performance Messungen](#Performance-Messungen)
- [Technische Anbindung](#Technische-Anbindung)
- [Kosten](#Kosten)
- [Fazit](#Fazit)
  
[Zurück zum Hauptmenu](../README.md)

## Modell Messungen
Betrachtet man die verschiedenen Auswertungen zusammen, kann folgendes festgehalten werden:
- Der Azure **Text Analytics Service** schneidet **insgesamt am besten ab**. 
  - Bei der Accuracy pro Sprache ist der Service bei Deutsch zwar nicht Spitzenreiter aber ansonsten ist die Trefferquote jeweils 
    am höchsten. 
  - Vor allem bei **wenig Text** (Accuracy per word) liefert der Service die **mit Abstand besten Werte** und erreicht schon ab sieben
   Worten eine Trefferquote von 95%.   
  - Bei den gemischten Texten in Deutsch, Französisch, Italienisch und Englisch erreicht der Service eine 
    **allgemeine Trefferquote von über 99%**. 
- **Gute Resultate** liefern auch die öffentlichen **LangDetect und LangDetectSpacy** Bibliotheken mit einer 
  **allgemeinen Trefferquote von rund 98.5%**.
- **LangFromStopwords** folgt knapp dahinter mit einer **allgemeinen Trefferquote von 97.8%**. 
  - Einzig beim Italienisch fällt die Bibliothek zurück. Das liegt aber sehr wahrscheinlich an den kleinen Wortliste.   
- Die **LangFromChars** Bibliothek **fällt mit einer allgemeinen Trefferquote von 95.2% deutlich ab**.

## Performance Messungen
Wenn man alle drei Performance Auswertungen betrachtet, muss man **unterscheiden** zwischen dem Azure Text Analytics 
Service und den anderen Bibliotheken. 

Azure Text Analytics Service:
- Der Azure Service läuft **remote**, das heisst **CPU** Auslastung und **Memory Peak** sind **gering**, dafür hat man 
  eine **langsame Antwortzeit**. 
- Die Messung der Antwortzeit erfolgte dabei je Aufruf. Azure bietet aber auch an, das mehrere Texte gleichzeitig 
  (mit einem Call) bearbeitet werden.
- Je nach Anwendungsscenario kann hier also die durchschnittliche **Antwortzeit**, mit Hilfe von **Batch Aufrufen**, 
  stark **verbessern**.

Bibliotheken:
- Hier fällt vor allem die **LangFromChars** Bibliothek mit **schlechten Werten** auf. Der CPU Verbrauch ist doppelt so 
  hoch und der Memory Peak fällt mehr als 250 mal höher aus.
- Die LangDetectSpacy Bibliothek ist etwas langsamer und benötigt mehr Speicher als die beiden anderen.
- Absoluten **Spitzenreiter** ist die **LangFromStopwords** Bibliothek, was auf die komplett **einfache Architektur** 
  zurückzuführen ist.

## Technische Anbindung
Die Anbindung der Bibliotheken ist technisch gut möglich. Der Ansatz mit der generischen Schnittstelle zeigt dies auf einfache Art und Weise und bietet zusätzlich die Möglichkeit eine Bibliothek ohne grosse Code Änderungen auszutauschen. 

Zu beachten ist, dass der Azure Text Analytics Service einen Internet Zugang benötigt, was je nach Anwendungsscenario eventuell nicht immer gegeben ist. Zudem sind die Ressourcen Anforderungen der einzelnen Bibliotheken sehr unterschiedlich.

## Kosten
Die öffentlichen Bibliotheken sind entweder als einer Apache Software oder MIT Lizenz verfügbar und können frei eingesetzt werden. Die Azure Text Analytics Service ist ein kommerzielles Angebot. Die Kosten ergeben sich aus dem Volumen und müssen daher je Anwendungsfall betrachtet werden.

## Fazit
Insgesamt überzeugen die beiden Bibliotheken LangFromStopwords und LangFromChars mit den verwendeten Testdaten nicht besonders. Falls Sie mit spezifischen Daten der Mobiliar nicht besser abschneiden steht mit der LangDetect Bibliothek eine gute, kostenlose Alternative zur Verfügung. Falls man umfangreiche NLP (Natural Language Processing) Aufgaben ausführen muss bietet Spacy eine grosse Sammlung von Modellen und Funktionen.

Wenn es Einschränkungen bei den Ressourcen (Zeit, Memory, CPU) gibt ist allenfalls die LangFromStopwords Bibliothek eine interessante Variante. Ausserdem kann das Modell durch anpassen der Wortlisten einfacher auf spezifisches Vokabular ausgerichtet werden als die anderen Bibliotheken. Für den Einsatz mit Italienisch müsste die aktuelle Lösung allerdings verbessert werden.

Der Azure Text Analytics Service schneidet insgesamt am besten ab. Dies ist vor allen bei der Spracherkennung mit wenig Text auffällig. Hier erreicht der Service die mit Abstand besten Werte. 

Ein interessanter Aspekt ist auch die Betrachtung der jeweilige Architektur. Der Ansatz mit der Wortliste (LangFromStopwords) kann zwar mit der Trefferquote nicht ganz vorne mithalten, ist aber in Sachen Performance der Spitzenreiter. Der Ansatz mit der Klassifizierung (LangDetect und LangDetectSpacy) schneidet gut ab, zeigt aber seine Limiten bei wenig Worten. Am meisten überzeugt der Azure Service mit den neuronalen Netzwerk Technologien. Das dies aber «per se» nicht so einfach ist, sieht man am Beispiel der LangFromChars Bibliothek.



---
[Zum Seitenanfang](#Ergebnisse)  &nbsp; | &nbsp;  [Zum Hauptmenu](../README.md)
