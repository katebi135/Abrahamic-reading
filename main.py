import streamlit as st
from datetime import date
from jafr_module import perform_jafr
from simiyya_module import perform_simiyya
from kimiya_module import perform_kimiya
from limiyya_module import perform_limiyya

st.set_page_config(page_title="Abrahamic Reading", layout="centered")
st.title("🔮 Abrahamic Reading Portal")
st.markdown("Welcome to the Abrahamic Reading experience – based on sacred numerology, symbolic archetypes, spiritual chemistry, and esoteric astrology.")

with st.form("user_form"):
    name = st.text_input("Your Full Name")
    mother_name = st.text_input("Mother's Name")
    birthdate = st.date_input("Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())
    birthplace = st.text_input("Place of Birth")
    submitted = st.form_submit_button("🧿 Generate Reading")

if submitted:
    st.success("🔓 Reading generated below.")
    st.markdown("---")

    jafr_result = perform_jafr(name, mother_name, birthdate)
    simiyya_result = perform_simiyya(name)
    kimiya_result = perform_kimiya(birthdate)
    limiyya_result = perform_limiyya(birthdate, birthplace)

    st.markdown("### 🧮 Jafr (Islamic Numerology)")
    st.write(jafr_result)

    st.markdown("### 🪞 Simiyya (Symbolic Reading)")
    st.write(simiyya_result)

    st.markdown("### ⚗️ Kimiya (Spiritual Chemistry)")
    st.write(kimiya_result)

    st.markdown("### 🌒 Limiyya (Astrology + Quranic Wisdom)")
    st.write(limiyya_result)

    st.markdown("---")
    st.info("This tool is for educational and esoteric exploration purposes only.")

