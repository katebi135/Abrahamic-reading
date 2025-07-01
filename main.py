import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Abrahamic Reading", layout="centered")
st.title("🔮 Abrahamic Reading Web App")
st.markdown("Welcome to the Abrahamic Reading experience – based on sacred numerology, lunar phases, and esoteric wisdom.")

with st.form("user_form"):
    st.header("Enter Your Information")

    # 🌐 Language Selection
    lang = st.selectbox("Select Language | زبان را انتخاب کنید | اختر اللغة", ["English", "Arabic", "Farsi"])

    # 👤 Personal Info
    name = st.text_input("Your name")
    mother_name = st.text_input("Mother's name")
    birthdate = st.date_input("Your date of birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())
    birthplace = st.text_input("Place of birth")

    # 👪 Family Information (Optional)
    st.subheader("Optional: Family Info")
    father_name = st.text_input("Father's name")
    father_dob = st.date_input("Father's date of birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())
    spouse_name = st.text_input("Spouse's name")
    spouse_dob = st.date_input("Spouse's date of birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())
    children_info = st.text_area("Children info (Name + birthdate, one per line)", placeholder="e.g. Fatemeh – 2017-01-16\nReza – 2020-05-01")

    # 🔮 Mystical Sciences Toggles
    st.subheader("Mystical Sciences to Include")
    include_jafr = st.checkbox("Jafr (Islamic Numerology)", value=True)
    include_simiyya = st.checkbox("Simiyya (Symbolic Reading)", value=True)
    include_kimiyya = st.checkbox("Kimiyya (Spiritual Chemistry)", value=True)
    include_limiyya = st.checkbox("Limiyya (Quran & Elemental Astrology)", value=True)

    submit = st.form_submit_button("🔵 Generate Reading")

if submit:
    st.success("🕯️ Reading complete. Scroll down for your mystical analysis.")

    # Collect selected modules
    selected_modules = []
    if include_jafr: selected_modules.append("Jafr (Islamic Numerology)")
    if include_simiyya: selected_modules.append("Simiyya (Symbolic Reading)")
    if include_kimiyya: selected_modules.append("Kimiyya (Spiritual Chemistry)")
    if include_limiyya: selected_modules.append("Limiyya (Quranic & Elemental Astrology)")

    st.markdown("### 📌 Summary of Provided Info")
    st.write(f"**Name:** {name}")
    st.write(f"**Mother's Name:** {mother_name}")
    st.write(f"**Date of Birth:** {birthdate}")
    st.write(f"**Place of Birth:** {birthplace}")
    
    if father_name:
        st.write(f"**Father's Name:** {father_name}")
    if spouse_name:
        st.write(f"**Spouse's Name:** {spouse_name}")
    if children_info:
        st.write(f"**Children Info:**\n{children_info}")

    st.markdown("### 🧿 Mystical Sciences Selected")
    for mod in selected_modules:
        st.markdown(f"✔️ {mod}")

    st.markdown("### 📜 Your Abrahamic Reading")
    st.info("🧬 This is a placeholder. Real mystical decoding will be added soon for each selected module.")

    st.markdown("---")
    st.info("✨ Disclaimer: For educational and entertainment purposes only.")
    st.caption("© Abrahamic Reading - All rights reserved.")
