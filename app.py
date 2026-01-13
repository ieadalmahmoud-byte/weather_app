import streamlit as st
import requests
from config import API_KEY # استدعاء المفتاح من الملف المنفصل
 
st.set_page_config(page_title="Weather App", layout="centered")
 
st.title("Streamlit Weather App – OpenWeatherMap Integration")
 
# واجهة اختيار نوع البحث كما في الوصف الوظيفي
search_mode = st.radio("Choose search mode:", ("City Name", "Latitude & Longitude"))
 
params = {"appid": API_KEY, "units": "metric"} # ضبط الوحدات للنظام المتري (Celsius)
 
if search_mode == "City Name":
    city = st.text_input("Enter city name (e.g., Berlin)")
    if city: params["q"] = city
else:
    col1, col2 = st.columns(2)
    with col1: lat = st.number_input("Latitude", format="%.4f")
    with col2: lon = st.number_input("Longitude", format="%.4f")
    params["lat"], params["lon"] = lat, lon
 
if st.button("Fetch Weather Data"):
    try:
        # جلب البيانات بالإنجليزية والألمانية كما هو مطلوب
        res_en = requests.get("https://api.openweathermap.org/data/2.5/weather", params={**params, "lang": "en"}).json()
        res_de = requests.get("https://api.openweathermap.org/data/2.5/weather", params={**params, "lang": "de"}).json()
 
        if res_en.get("cod") == 200:
            st.success(f"Location: {res_en['name']}") # عرض اسم الموقع
            st.metric("Temperature", f"{res_en['main']['temp']} °C") # عرض الحرارة بالسليزيوس
            
            # عرض الوصف باللغتين
            st.write(f"**Description (EN):** {res_en['weather'][0]['description']}")
            st.write(f"**Description (DE):** {res_de['weather'][0]['description']}")
        else:
            st.error(f"Error: {res_en.get('message')}")
    except Exception as e:
        st.error(f"Connection error: {e}")
 