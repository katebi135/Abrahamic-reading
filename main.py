
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
