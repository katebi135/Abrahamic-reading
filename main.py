import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Abrahamic Reading Web App", layout="centered")

st.title("🔮 Abrahamic Reading Web App")

with st.form("user_form"):
    st.header("Enter Your Information")

    # 📌 Personal Info
    name = st.text_input("Your name")
    mother_name = st.text_input("Mother’s name")
    birthdate = st.date_input("Your date of birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())
    birthplace = st.text_input("Place of birth")

    # 👪 Optional Family Fields
    st.subheader("Optional: Family Info")
    father_name = st.text_input("Father’s name")
    father_dob = st.date_input("Father’s date of birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())

    spouse_name = st.text_input("Spouse’s name")
    spouse_dob = st.date_input("Spouse’s date of birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())

    children_info = st.text_area("Children (name + birthdate, one per line)", placeholder="e.g. Fatemeh – 2017-01-16\nReza – 2020-05-01")

    # 🔮 Mystical Modules Toggle
    st.subheader("Mystical Sciences to Include")
    include_jafr = st.checkbox("Jafr (Islamic Numerology)", value=True)
    include_simiya = st.checkbox("Sīmiyāʾ (Symbolic Reading)", value=True)
    include_kimiya = st.checkbox("Kīmiyāʾ (Spiritual Chemistry)", value=True)
    include_limiya = st.checkbox("Līmiyāʾ (Lunar & Elemental Astrology)", value=True)

    # 🚀 Submit
    submit = st.form_submit_button("✨ Generate Reading")

# ✅ Output Display Block
if submit:
    st.success("🔓 Abrahamic Insight Unlocked")

    st.markdown(f"### 🧑 Name: {name}")
    st.markdown(f"**👵 Mother’s Name:** {mother_name}")
    st.markdown(f"**🎂 Date of Birth:** {birthdate}")
    st.markdown(f"**🌍 Place of Birth:** {birthplace}")

    if father_name:
        st.markdown(f"**👨 Father:** {father_name} ({father_dob})")
    if spouse_name:
        st.markdown(f"**💍 Spouse:** {spouse_name} ({spouse_dob})")
    if children_info:
        st.markdown("**👶 Children:**")
        for child in children_info.strip().split("\n"):
            st.markdown(f"• {child}")

    st.markdown("### 🧿 Mystical Sciences Selected:")
    if include_jafr:
        st.markdown("- ✅ Jafr (Islamic Numerology)")
    if include_simiya:
        st.markdown("- ✅ Sīmiyāʾ (Symbolic Reading)")
    if include_kimiya:
        st.markdown("- ✅ Kīmiyāʾ (Spiritual Chemistry)")
    if include_limiya:
        st.markdown("- ✅ Līmiyāʾ (Lunar & Elemental Astrology)")

    st.info("🔗 Advanced reading coming soon…")
