
import streamlit as st
from datetime import date
import moon_logic
from compatibility_module import symbolic_analysis, get_kimiyaa_insight, get_quranic_verse
# You can add other imports like app.py functions if needed

st.set_page_config(page_title="🪬 Abrahamic Reading Portal", layout="centered")

st.title("🔮 Abrahamic Reading Portal")
st.markdown("Welcome to the Abrahamic Reading experience – based on sacred numerology, symbolic archetypes, spiritual chemistry, and esoteric astrology.")

with st.form("user_form"):
    name = st.text_input("Your Full Name")
    mother_name = st.text_input("Mother's Name")
    father_name = st.text_input("Father's Name")
    birthdate = st.date_input("Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())
    birthplace = st.text_input("Place of Birth")

    jafr = st.checkbox("📿 Jafr (Islamic Numerology)", value=True)
    simiyya = st.checkbox("🪬 Simiyya (Symbolic Reading)", value=True)
    kimiyaa = st.checkbox("⚗️ Kimiyaa (Spiritual Chemistry)", value=True)
    limiyya = st.checkbox("🌙 Limiyya (Quranic + Elemental Astrology)", value=True)

    submitted = st.form_submit_button("🧿 Generate Reading")

if submitted:
    st.success("✅ Reading generated below.")

    if jafr:
        name_sum = sum(ord(c) for c in name if c.isalpha())
        mother_sum = sum(ord(c) for c in mother_name if c.isalpha())
        father_sum = sum(ord(c) for c in father_name if c.isalpha())
        root_number = name_sum % 9 or 9

        st.markdown("### 📿 Jafr (Islamic Numerology)")
        st.code(f"""Name Numeric Value: {name_sum}
Mother Name Value: {mother_sum}
Father Name Value: {father_sum}
Root Number (based on your name): {root_number}""")

        st.write(f"✨ Interpretation: Frequency resonance on the divine number {root_number}")

    if simiyya:
        symbols = symbolic_analysis(name, mother_name)
        st.markdown("### 🪬 Simiyya (Symbolic Reading)")
        st.write("**Symbolic Roles:**")
        st.json(symbols)
        st.write(f"🔮 Dominant Trait: `{symbols[0] if symbols else 'Unknown'}`")

    if kimiyaa:
        essence, alchemy = get_kimiyaa_insight(name, mother_name, birthdate)
        st.markdown("### ⚗️ Kimiyaa (Spiritual Chemistry)")
        st.write(f"**Elemental Essence**: {essence}")
        st.write(f"**Spiritual Alchemy**: {alchemy}")

    if limiyya:
        phase = calculate_lunar_phase(birthdate)
        verse = get_quranic_verse(birthdate)
        st.markdown("### 🌙 Limiyya (Astrology + Quranic Wisdom)")
        st.write(f"🌖 **Lunar Phase at Birth**: {phase}")
        st.write(f"📖 **Verse**: {verse}")

    st.markdown("---")
    st.info("📌 Disclaimer: This tool is for educational and entertainment purposes only.")
    st.caption("© Abrahamic Reading AI — All rights reserved.")
