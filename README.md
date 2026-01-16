# Wetter-Analyse-System mit Sentiment-Integration
 
Dieses Projekt ist eine fortschrittliche interaktive Webanwendung, die mit Python und dem Streamlit-Framework entwickelt wurde. Die App kombiniert Echtzeit-Wetterdaten mit modernster Sentiment-Analyse, um die emotionale Wirkung der Wetterlage auf den Benutzer zu erfassen und zu archivieren.
 
## Hauptfunktionen (Erweiterte Version)
 
- **Echtzeit-Wetterabfrage:** Abruf aktueller Wetterdaten (Temperatur, Wetterzustand) über die OpenWeatherMap API durch Eingabe des Stadtnamens.
- **Sentiment-Analyse:** Integration der TextBlob-Bibliothek zur mathematischen Analyse von Benutzerkommentaren (Berechnung des Polaritätsscores).
- **Lokale Datenpersistenz:** Automatische Speicherung der Wetterdaten, Benutzerkommentare und Analyseergebnisse in einer lokalen SQLite-Datenbank (`weather_sentiment.db`).
- **Dynamischer Verlauf:** Visualisierung der letzten Abfragen und Feedbacks in einer interaktiven Seitenleiste (Sidebar).
- **Mehrsprachige Unterstützung:** Die Benutzeroberfläche und die Wetterbeschreibungen sind vollständig in deutscher Sprache lokalisiert.
 
## Technische Highlights
 
- **Backend:** Python 3.x
- **Frontend:** Streamlit
- **Datenbank:** SQLite3
- **NLP (Natural Language Processing):** TextBlob für die Stimmungsanalyse
- **Sicherheit:** Trennung sensibler Daten (API-Schlüssel) in einer separaten `config.py` Datei.
 
## Installationsanleitung
 
1. Klonen Sie das Repository:
   ```bash
   git clone [https://github.com/ieadalmahmoud-byte/weather_app.git](https://github.com/ieadalmahmoud-byte/weather_app.git)
 
