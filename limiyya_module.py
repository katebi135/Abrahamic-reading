def get_astrological_profile(dob, place: str) -> dict:
    zodiac = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
              "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    return {
        "Zodiac Sign": zodiac[dob.month % 12],
        "Place of Birth": place
    }
