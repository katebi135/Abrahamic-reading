import streamlit as st
from datetime import datetime

st.title("🔮 Abrahamic Reading Web App")

with st.form("user_form"):
    st.header("Enter Your Information")

    # Personal Info
    name = st.text_input("Your name")
    mother_name = st.text_input("Mother’s name")
    birthdate = st.date_input("Your date of birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())
    birthplace = st.text_input("Place of birth")

    # Optional Family Fields
    st.subheader("Optional: Family Info")
    father_name = st.text_input("Father’s name")
    father_dob = st.date_input("Father’s date of birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())

    spouse_name = st.text_input("Spouse’s name")
    spouse_dob = st.date_input("Spouse’s date of birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())

    children_info = st.text_area("Children (name - birthdate, one per line)", placeholder="e.g.\nFatemeh - 2017-01-16\nReza - 2020-05-01")

    # Mystical Modules Toggle
    st.subheader("Mystical Sciences to Include")
    include_jafr = st.checkbox("Jafr (Islamic Numerology)", value=True)
    include_simiya = st.checkbox("Simiyā (Symbolic Reading)", value=True)
    include_kimiya = st.checkbox("Kīmiyā (Spiritual Chemistry)", value=True)
    include_limiya = st.checkbox("Līmiyāʾ (Lunar & Elemental Astrology)", value=True)

    submit = st.form_submit_button("🔍 Generate Reading")

if submit:
    st.success("🔓 Reading Unlocked")
    
    st.write(f"🧑 Name: {name}")
    st.write(f"👵 Mother: {mother_name}")
    st.write(f"🎂 DOB: {birthdate}")
    st.write(f"🌍 Birthplace: {birthplace}")

    if father_name:
        st.write(f"👨 Father: {father_name} ({father_dob})")
    if spouse_name:
        st.write(f"💍 Spouse: {spouse_name} ({spouse_dob})")
    if children_info:
        st.write("👶 Children:")
        for line in children_info.split("\n"):
            if line.strip():
                st.write(f"• {line.strip()}")

    st.write("🔮 Modules selected:")
    if include_jafr: st.write("✔️ Jafr")
    if include_simiya: st.write("✔️ Simiyā")
    if include_kimiya: st.write("✔️ Kīmiyā")
    if include_limiya: st.write("✔️ Līmiyāʾ")

    # Here you can call your logic modules for numerology, Jafr, Simiyā, etc.

import streamlit as st
from compatibility_module import basic_name_numerology
from moon_logic import get_moon_phase
from datetime import datetime

st.set_page_config(page_title="Abrahamic Reading", layout="centered")

st.title("🔮 Abrahamic Reading Web App")

# Language selector
lang = st.selectbox("Select language / زبان را انتخاب کنید", ["English", "فارسی"])

# Input fields
name = st.text_input("Enter your name" if lang == "English" else "نام خود را وارد کنید")
mother_name = st.text_input("Enter your mother’s name" if lang == "English" else "نام مادر خود را وارد کنید")
birthdate = st.date_input("Your birthdate" if lang == "English" else "تاریخ تولد شما")

if st.button("Generate Reading" if lang == "English" else "استخراج فال"):
    if not name or not mother_name:
        st.warning("Please fill all fields" if lang == "English" else "لطفاً تمام فیلدها را پر کنید")
    else:
        st.subheader("🧮 Numerology Result" if lang == "English" else "نتیجه علم اعداد")
        value = basic_name_numerology(name + mother_name)
        st.write(f"Numeric value: {value}")

        st.subheader("🌙 Moon Phase on Your Birthday" if lang == "English" else "مرحله ماه در تاریخ تولد شما")
        moon = get_moon_phase(birthdate)
        st.write(moon)

        st.subheader("📖 Qur'anic Insight (Ism A'zam)" if lang == "English" else "آیه مرتبط با اسم اعظم")
        # Placeholder output
        st.write("اللَّهُ نُورُ السَّمَاوَاتِ وَالْأَرْضِ" if lang == "English" else "اللَّهُ نُورُ السَّمَاوَاتِ وَالْأَرْضِ")

        st.success("Reading complete" if lang == "English" else "فال استخراج شد")
