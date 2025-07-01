import streamlit as st
from datetime import date

st.set_page_config(page_title="Abrahamic Reading", layout="centered")

st.title("🔮 Abrahamic Reading Portal")
st.markdown("Welcome to the Abrahamic Reading experience – based on sacred numerology, lunar phases, and esoteric wisdom.")

with st.form("user_form"):
    name = st.text_input("Your Full Name")
    mother_name = st.text_input("Mother's Name")
    birthdate = st.date_input("Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())
    birthplace = st.text_input("Place of Birth")

    submitted = st.form_submit_button("🔍 Generate Reading")

if submitted:
    st.success("✅ Reading generated below.")

    # Simple test numerology logic
    name_sum = sum(ord(char) for char in name if char.isalpha())
    root_number = name_sum % 9 or 9

    st.markdown("### 🔢 Numerology Reading")
    st.write(f"Hello **{name}**, your name's numerical value is `{name_sum}`, and your root number is **{root_number}**.")

    st.markdown("### 🌙 Sample Daily Qur’anic Verse (placeholder)")
    st.write("**اللَّهُ نُورُ السَّمَاوَاتِ وَالْأَرْضِ** (Allah is the Light of the heavens and the earth) – Surah An-Nur 24:35")

    st.markdown("### 💡 More features coming:")
    st.write("- Daily verse + tafsir")
    st.write("- Relationship synchronicity")
    st.write("- Red Jafr analysis")
    st.write("- Personalized spiritual recommendations")

    st.markdown("---")
    st.info("✨ Disclaimer: This tool is for educational and entertainment purposes only.")
    st.caption("© Abrahamic Reading - All rights reserved.")
