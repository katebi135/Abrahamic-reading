
def perform_kimiya(birthdate):
    elements = ["Air", "Fire", "Water", "Earth"]
    index = (birthdate.day + birthdate.month) % 4
    return {
        "Dominant Element": elements[index],
        "Spiritual Alchemy": f"Your essence harmonizes with {elements[index]}, indicating inner {['clarity','passion','intuition','stability'][index]}."
    }
