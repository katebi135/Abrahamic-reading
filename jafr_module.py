
# jafr_module.py

def name_to_number(name: str) -> int:
    # Simple Abjad (Jafr) calculation using basic letter-to-number values (Arabic)
    abjad_table = {
        'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9,
        'ي': 10, 'ک': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80,
        'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600,
        'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
    }

    name = name.replace(" ", "").replace("‌", "").strip()
    total = 0
    for char in name:
        if char in abjad_table:
            total += abjad_table[char]
    return total
