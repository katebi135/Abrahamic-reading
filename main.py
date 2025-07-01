import streamlit as st
from datetime import date

# Set page config
st.set_page_config(page_title="Abrahamic Reading", layout="centered")

# Title and intro
st.title("🕋 Abrahamic Reading Portal")
st.markdown("""
Welcome to the Abrahamic Reading experience — combining the mystical sciences of **Jafr** (Islamic numerology), **Simiyya** (symbolic vision), **Kimiya** (spiritual transformation), and **Limiyya** (elemental Qur'anic astrology).
""")

# User form input
with st.form("user_form"):
    st.header("🔮 Input Your Information")
    name = st.text_input("🧵 Your Full Name")
    mother_name = st.text_input("👩 Mother's Name")
    birthdate = st.date_input("📅 Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())
    birthplace = st.text_input("📍 Place of Birth")

    st.header("🧬 Mystical Sciences to Include")
    jafr = st.checkbox("🔢 Jafr (Islamic Numerology)", value=True)
    simiyya = st.checkbox("🧿 Simiyya (Symbolic Reading)", value=True)
    kimiya = st.checkbox("⚗️ Kimiya (Spiritual Chemistry)", value=True)
    limiyya = st.checkbox("🌙 Limiyya (Quran & Elemental Astrology)", value=True)

    submitted = st.form_submit_button("🔮 Generate Reading")

# If form submitted
if submitted:
    st.success("✅ Reading generated below.")
    st.subheader("📌 Summary of Input")
    st.write(f"**Name:** {name}")
    st.write(f"**Mother's Name:** {mother_name}")
    st.write(f"**Birthdate:** {birthdate}")
    st.write(f"**Birthplace:** {birthplace}")

    # Display modules selected
    st.subheader("📚 Modules Selected:")
    st.markdown(f"- Jafr: **{jafr}**")
    st.markdown(f"- Simiyya: **{simiyya}**")
    st.markdown(f"- Kimiya: **{kimiya}**")
    st.markdown(f"- Limiyya: **{limiyya}**")

    # 🔢 Simple numerology logic (Jafr style)
    if jafr:
        name_sum = sum(ord(c) for c in name if c.isalpha())
        root_number = name_sum % 9 or 9
        st.subheader("🔢 Jafr Numerology")
        st.write(f"Your name value is **{name_sum}**, Root number is **{root_number}**")

    if simiyya:
        st.subheader("🧿 Simiyya (Symbolism)")
        st.write("You're under the archetype of a **Seeker of Hidden Truth** based on symbolic signature.")

    if kimiya:
        st.subheader("⚗️ Kimiya (Spiritual Chemistry)")
        st.write("Your spiritual element is **Water**, indicating deep intuition and emotional wisdom.")

    if limiyya:
        st.subheader("🌙 Limiyya (Qur'anic Elemental Reading)")
        st.markdown("**Verse:** 'اللَّهُ نُورُ السَّمَاوَاتِ وَالْأَرْضِ' (An-Nur 24:35)")

    st.markdown("---")
    st.info("🧘 This tool is for educational and spiritual entertainment only.")
