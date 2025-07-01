def get_spiritual_elements(value: int) -> dict:
    elements = ["Water", "Fire", "Air", "Earth"]
    alchemy = ["Mercury", "Sulfur", "Salt", "Spirit"]
    return {
        "Dominant Element": elements[value % 4],
        "Spiritual Alchemy": alchemy[value % 4]
    }
