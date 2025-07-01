
def perform_simiyya(name):
    char_traits = {
        "a": "Leader", "b": "Healer", "c": "Seeker", "d": "Builder", "e": "Artist",
        "f": "Fighter", "g": "Mystic", "h": "Defender", "i": "Visionary"
    }
    meanings = [char_traits.get(c.lower(), "Wanderer") for c in name if c.isalpha()]
    return {
        "Symbolic Roles": meanings,
        "Dominant Trait": max(set(meanings), key=meanings.count)
    }
