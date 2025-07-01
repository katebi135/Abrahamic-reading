import streamlit as st
from jafr_module import name_to_number, get_jafr_insight
from simiyya_module import get_symbolic_reading
from kimiya_module import get_spiritual_elements
from limiyya_module import get_astrological_profile
from moon_logic import calculate_lunar_phase

st.set_page_config(page_title="Abrahamic Reading Portal", layout="centered")

st.title("🔮 Abrahamic Reading Portal")
st.markdown("Welcome to the Abrahamic Reading experience – based on sacred numerology, symbolic archetypes, spiritual chemistry, and esoteric astrology.")

with st.form("reading_form"):
    name = st.text_input("Your Full Name")
    mother_name = st.text_input("Mother's Name")
    dob = st.date_input("Date of Birth")
    mother_dob = st.date_input("Mother's Date of Birth")
    father_name = st.text_input("Father's Name")
    father_dob = st.date_input("Father's Date of Birth")
    place_of_birth = st.text_input("Place of Birth")
    children_names = st.text_area("Children (comma-separated)")
    submitted = st.form_submit_button("🔮 Generate Reading")

if submitted:
    st.success("✅ Reading generated below.")
    name_value = name_to_number(name)
    mother_value = name_to_number(mother_name)
    jafr_result = get_jafr_insight(name_value, mother_value)
    st.subheader("📜 Jafr (Islamic Numerology)")
    st.code(jafr_result, language="python")

    st.subheader("🌟 Simiyya (Symbolic Reading)")
    st.write(get_symbolic_reading(name_value))

    st.subheader("🧪 Kimiya (Spiritual Chemistry)")
    st.write(get_spiritual_elements(name_value))

    st.subheader("🪐 Limiyya (Astrology + Quranic Wisdom)")
    st.write(get_astrological_profile(dob, place_of_birth))

    st.subheader("🌙 Lunar Phase at Birth")
    st.write(calculate_lunar_phase(dob))
