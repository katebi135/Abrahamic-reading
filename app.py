
import streamlit as st
from datetime import datetime
from hijri_converter import convert
import convertdate.jalali

st.set_page_config(page_title="Abrahamic Reading", layout="centered")

st.title("🔮 Abrahamic Reading Portal")
st.markdown("Welcome to the Abrahamic Reading experience – sacred numerology, lunar phases, and esoteric wisdom.")

with st.form("user_form"):
    full_name = st.text_input("Full Name")
    dob = st.date_input("Your Date of Birth")
    father_name = st.text_input("Father's Name")
    father_dob = st.date_input("Father's Date of Birth")
    mother_name = st.text_input("Mother's Name")
    mother_dob = st.date_input("Mother's Date of Birth")

    children_names = st.text_area("Children's Names (one per line)")
    children_dobs = st.text_area("Children's DOBs (YYYY-MM-DD format, one per line matching the names)")

    language = st.selectbox("Preferred Language", ["English", "Arabic", "Farsi"])

    submit = st.form_submit_button("Get Your Reading")

if submit:
    st.subheader("📜 Your Abrahamic Reading Summary")
    st.markdown(f"**Name:** {full_name}")
    st.markdown(f"**Date of Birth (Gregorian):** {dob.strftime('%Y-%m-%d')}")

    # Hijri Conversion
    hijri_date = convert.Gregorian(dob.year, dob.month, dob.day).to_hijri()
    st.markdown(f"**Date of Birth (Hijri):** {hijri_date}")

    # Shamsi Conversion
    jalali_date = convertdate.jalali.from_gregorian(dob.year, dob.month, dob.day)
    st.markdown(f"**Date of Birth (Shamsi):** {jalali_date[0]}/{jalali_date[1]}/{jalali_date[2]}")

    st.markdown(f"**Father:** {father_name}, Born: {father_dob}")
    st.markdown(f"**Mother:** {mother_name}, Born: {mother_dob}")

    children_list = children_names.split("\n")
    dob_list = children_dobs.split("\n")

    st.markdown("**Children:**")
    for name, dob in zip(children_list, dob_list):
        st.markdown(f"- {name} ({dob})")

    st.info("✨ Disclaimer: For educational and entertainment purposes only.")
