
def basic_name_numerology(name):
    # Very basic Abjad-style numerology (sum of letter Unicode values)
    total = sum(ord(c) for c in name if c.isalpha())
    return total
