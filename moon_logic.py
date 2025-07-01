
# moon_logic.py

def get_moon_phase(birthdate):
    # Simple moon phase based on day of the month (placeholder logic)
    day = birthdate.day
    phases = [
        "🌑 New Moon",
        "🌒 Waxing Crescent",
        "🌓 First Quarter",
        "🌔 Waxing Gibbous",
        "🌕 Full Moon",
        "🌖 Waning Gibbous",
        "🌗 Last Quarter",
        "🌘 Waning Crescent"
    ]
    return phases[day % 8]
