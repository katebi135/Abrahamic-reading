def get_symbolic_reading(value: int) -> dict:
    traits = ["Wanderer", "Seeker", "Guardian", "Healer", "Scribe", "Leader", "Mystic"]
    return {
        "Symbolic Role": traits[value % len(traits)],
        "Trait Frequency": traits[:(value % len(traits)) + 1]
    }
