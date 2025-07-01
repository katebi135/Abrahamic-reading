import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Abrahamic Reading", layout="centered")
st.title("🔮 Abrahamic Reading Web App")

with st.form("user_form"):
    st.header("Enter Your Information")

    # 🌍 Language Selection
    lang = st.selectbox("Select language / زبان را انتخاب کنید", ["English", "Arabic", "Farsi"])

    # 🧍 Personal Info
    name = st.text_input("Your name")
    mother_name = st.text_input("Mother’s name")
    birthdate = st.date_input("Your date of birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())
    birthplace = st.text_input("Place of birth")

    # 👨‍👩‍👧 Family Information
    st.subheader("Optional: Family Info")
    father_name = st.text_input("Father’s name")
    father_dob = st.date_input("Father’s date of birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())
    spouse_name = st.text_input("Spouse’s name")
    spouse_dob = st.date_input("Spouse’s date of birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())
    children_info = st.text_area("Children (Name + birthdate, one per line)", 
                                 placeholder="e.g. Fatemeh – 2017-01-16\nReza – 2020-05-01")

    # 🧙 Mystical Sciences Toggles
    st.subheader("Mystical Sciences to Include")
    include_jafr = st.checkbox("Jafr (Islamic Numerology)", value=True)
    include_simiyya = st.checkbox("Simiyya (Symbolic Reading)", value=True)
    include_kimiyya = st.checkbox("Kimiyya (Spiritual Chemistry)", value=True)
    include_limiyya = st.checkbox("Limiyya (Quran & Elemental Astrology)", value=True)

    submit = st.form_submit_button("🧿 Generate Reading")

if submit:
    st.success("Your request is processing...")
    st.write("📜 Name:", name)
    st.write("👩 Mother:", mother_name)
    st.write("📅 Birthdate:", birthdate)
    st.write("📍 Birthplace:", birthplace)
    st.write("👨 Father:", father_name)
    st.write("❤️ Spouse:", spouse_name)
    st.write("🧒 Children Info:", children_info)
    st.write("🔮 Modules Selected:")
    st.write("- Jafr:", include_jafr)
    st.write("- Simiyya:", include_simiyya)
    st.write("- Kimiyya:", include_kimiyya)
    st.write("- Limiyya:", include_limiyya)
