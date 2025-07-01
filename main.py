
import streamlit as st
from datetime import date, datetime

import moon_logic
import jafr_module
import simiyya_module
import kimiya_module
import limiyya_module

st.set_page_config(page_title="🔮 Abrahamic Reading", layout="centered")

st.title("🔮 Abrahamic Reading Portal")
st.markdown("Welcome to the Abrahamic Reading experience – based on sacred numerology, symbolic archetypes, spiritual chemistry, and esoteric astrology.")

with st.form("user_form"):
    name = st.text_input("Your Full Name")
    mother_name = st.text_input("Mother's Name")
    father_name = st.text_input("Father's Name (optional)")
    birthdate = st.date_input("Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())
    birthplace = st.text_input("Place of Birth")
    submitted = st.form_submit_button("🧿 Generate Reading")

if submitted:
    st.success("📖 Reading generated below.")

    # === Jafr Reading ===
    name_value = jafr_module.name_to_number(name)
    mother_value = jafr_module.name_to_number(mother_name)
    jafr_result = jafr_module.get_jafr_insight(name_value, mother_value)

    st.markdown("### 🧮 Jafr (Islamic Numerology)")
    st.code(f"Name Numeric Value: {name_value}\nMother Name Value: {mother_value}\nInterpretation: {jafr_result}")

    # === Simiyya Reading ===
    symbolic_roles = simiyya_module.generate_symbols(name)
    st.markdown("### 🪬 Simiyya (Symbolic Reading)")
    st.json({"Symbolic Roles": symbolic_roles, "Dominant Trait": symbolic_roles[0] if symbolic_roles else "Unknown"})

    # === Kimiya Reading ===
    element, alchemy = kimiya_module.get_alchemy_traits(name)
    st.markdown("### ⚗️ Kimiya (Spiritual Chemistry)")
    st.write(f"**Dominant Element:** {element}")
    st.write(f"**Spiritual Alchemy:** {alchemy}")

    # === Limiyya Reading ===
    moon_phase = moon_logic.calculate_lunar_phase(birthdate)
    limiyya_output = limiyya_module.extract_astrological_insight(birthdate, moon_phase)
    st.markdown("### 🌙 Limiyya (Astrology + Quranic Wisdom)")
    st.write(f"**Lunar Phase at Birth:** {moon_phase}")
    st.write(f"**Quranic Insight:** {limiyya_output}")

    st.markdown("---")
    st.info("🔖 Disclaimer: This tool is for educational and entertainment purposes only.")
    st.caption("© Abrahamic Reading App – All rights reserved.")
