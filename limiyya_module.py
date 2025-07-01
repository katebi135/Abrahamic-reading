
def perform_limiyya(birthdate, birthplace):
    verse = "اللَّهُ نُورُ السَّمَاوَاتِ وَالْأَرْضِ - Surah An-Nur 24:35"
    moon_phase = ["New Moon", "First Quarter", "Full Moon", "Last Quarter"][(birthdate.day % 4)]
    return {
        "Moon Phase at Birth": moon_phase,
        "Qur’anic Verse Guidance": verse,
        "Esoteric Note": f"Born under the {moon_phase}, you are spiritually drawn to deep transformation in {birthplace}."
    }
