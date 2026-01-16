import streamlit as st
import requests
import sqlite3
from textblob import TextBlob
from datetime import datetime
from config import API_KEY
 
# 1. Database Initialization
def init_db():
    conn = sqlite3.connect('weather_sentiment.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history 
                 (city TEXT, temp REAL, description TEXT, user_text TEXT, sentiment REAL, date TEXT)''')
    conn.commit()
    conn.close()
 
init_db()
 
# 2. UI Configuration
st.set_page_config(page_title="Professional Weather App", layout="wide")
st.title("Weather & Sentiment Analysis Tool 🌦️")
 
# Sidebar for History
st.sidebar.header("📜 Verlauf (History)")
 
# Input Section
stadt = st.text_input("Geben Sie den Stadtnamen ein (z.B. Leipzig):")
 
if st.button("Wetterdaten abrufen"):
    params = {"q": stadt, "appid": API_KEY, "units": "metric", "lang": "de"}
    try:
        res = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params).json()
        if res.get("cod") == 200:
            # Save weather data to session state
            st.session_state['current_weather'] = res
        else:
            st.error(f"Fehler: {res.get('message')}")
    except Exception as e:
        st.error(f"Verbindungsfehler: {e}")
 
# 3. Sentiment Analysis Section (This will appear ONLY after weather data is fetched)
if 'current_weather' in st.session_state:
    weather = st.session_state['current_weather']
    
    # Display Results
    st.success(f"Standort gefunden: {weather['name']}")
    st.metric("Temperatur", f"{weather['main']['temp']} °C")
    st.write(f"**Zustand:** {weather['weather'][0]['description']}")
    
    st.divider() # Visual separator
    
    # --- USER SENTIMENT INPUT AREA ---
    st.subheader("💬 Ihr Kommentar zum Wetter")
    user_text = st.text_area("Wie fühlen Sie sich bei diesem Wetter?", placeholder="Schreiben Sie hier...")
    
    if st.button("Feedback speichern"):
        if user_text:
            # Sentiment Analysis using TextBlob
            blob = TextBlob(user_text)
            score = blob.sentiment.polarity
            
            # Classification
            if score > 0: status = "Positiv 😊"
            elif score < 0: status = "Negativ ☹️"
            else: status = "Neutral 😐"
            
            st.info(f"Analyse: Ihr Feedback ist {status} (Score: {score})")
            
            # Save to SQLite Database
            conn = sqlite3.connect('weather_sentiment.db')
            c = conn.cursor()
            c.execute("INSERT INTO history VALUES (?, ?, ?, ?, ?, ?)", 
                      (weather['name'], 
                       weather['main']['temp'], 
                       weather['weather'][0]['description'], 
                       user_text, score, datetime.now().strftime("%Y-%m-%d %H:%M")))
            conn.commit()
            conn.close()
            st.success("Daten erfolgreich gespeichert!")
        else:
            st.warning("Bitte geben Sie zuerst einen Text ein.")
 
# 4. Display History in Sidebar
try:
    conn = sqlite3.connect('weather_sentiment.db')
    history_data = conn.execute("SELECT * FROM history ORDER BY date DESC LIMIT 5").fetchall()
    for entry in history_data:
        st.sidebar.write(f"**{entry[0]}**: {entry[1]}°C")
        st.sidebar.caption(f"Gefühl: {entry[3]}")
    conn.close()
except:
    pass
 