import requests 
import streamlit as st


st.title("AL_QURAN APP")


mariSurahsList =requests.get("https://api.alquran.cloud/v1/surah")

surahs=mariSurahsList.json()["data"]


optionsSurahs=[]
for s in surahs:
    optionsSurahs.append(f"{s["number"]} | {s["englishName"]} | {s["name"]} | {s["englishNameTranslation"]} | {s["numberOfAyahs"]} | {s["revelationType"]}")




item =st.selectbox("Choose The Surah",optionsSurahs)
surahNumber=item.split("|")[0].strip()





mariAyahsList =requests.get(f"https://api.alquran.cloud/v1/surah/{surahNumber}/ar.abdurrhmaansudais")
ayahs=mariAyahsList.json()["data"]["ayahs"]



for a in ayahs:
    st.write("Number:", a["number"])
    st.write("Text:", a["text"])
    st.write("Number in Surah:", a["numberInSurah"])
    st.write("Juz:", a["juz"])
    st.write("Manzil:", a["manzil"])
    st.write("Page:", a["page"])
    st.write("Ruku:", a["ruku"])
    st.write("Hizb Quarter:", a["hizbQuarter"])
    st.write("Sajda:", a["sajda"])
    st.divider()
    
             








    