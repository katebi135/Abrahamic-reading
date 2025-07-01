
def perform_jafr(name, mother_name, birthdate):
    name_value = sum(ord(c) for c in name if c.isalpha())
    mother_value = sum(ord(c) for c in mother_name if c.isalpha())
    root_number = (name_value + mother_value + birthdate.day + birthdate.month + birthdate.year) % 9 or 9
    return {
        "Name Numeric Value": name_value,
        "Mother Name Value": mother_value,
        "Root Number": root_number,
        "Interpretation": f"Your spiritual frequency resonates with the divine number {root_number}."
    }
