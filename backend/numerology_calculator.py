"""
Numerology Calculator untuk NEWME
Menentukan personality type dan element berdasarkan tanggal lahir
"""
from datetime import datetime

# Mapping numerology number ke personality + element
NUMEROLOGY_MAPPING = {
    1: {"personality": "Introvert", "element": "logam"},
    2: {"personality": "Extrovert", "element": "api"},
    3: {"personality": "Introvert", "element": "tanah"},
    4: {"personality": "Extrovert", "element": "tanah"},
    5: {"personality": "Introvert", "element": "api"},
    6: {"personality": "Extrovert", "element": "kayu"},
    7: {"personality": "Introvert", "element": "kayu"},
    8: {"personality": "Extrovert", "element": "logam"},
    9: {"personality": "Ambivert", "element": "air"}
}


def reduce_to_single_digit(number: int) -> int:
    """Reduce number to single digit by summing digits"""
    while number > 9:
        number = sum(int(digit) for digit in str(number))
    return number


def calculate_numerology_from_birthdate(birthdate_str: str) -> dict:
    """
    Calculate numerology number from birthdate
    
    Args:
        birthdate_str: Date string in format "YYYY-MM-DD" or datetime object
    
    Returns:
        dict with numerology_number, personality_type, and element
        
    Example:
        "2012-12-19" -> 19-12-2012
        Day: 19 -> 1+9 = 10 -> 1+0 = 1
        Month: 12 -> 1+2 = 3
        Year: 2012 -> 2+0+1+2 = 5 -> 5
        Total: 1 + 3 + 5 = 9
        Result: 9 = Ambivert AIR
    """
    try:
        # Parse birthdate
        if isinstance(birthdate_str, datetime):
            birth_date = birthdate_str
        else:
            # Try different date formats
            for fmt in ["%Y-%m-%d", "%d-%m-%Y", "%Y/%m/%d", "%d/%m/%Y"]:
                try:
                    birth_date = datetime.strptime(birthdate_str, fmt)
                    break
                except ValueError:
                    continue
            else:
                # Default fallback
                return {
                    "numerology_number": 5,
                    "personality_type": "Introvert",
                    "element": "api",
                    "calculation_steps": "Invalid date format"
                }
        
        day = birth_date.day
        month = birth_date.month
        year = birth_date.year
        
        # Reduce each to single digit
        day_reduced = reduce_to_single_digit(day)
        month_reduced = reduce_to_single_digit(month)
        year_reduced = reduce_to_single_digit(year)
        
        # Sum and reduce to single digit
        total = day_reduced + month_reduced + year_reduced
        final_number = reduce_to_single_digit(total)
        
        # Get personality + element from mapping
        mapping = NUMEROLOGY_MAPPING.get(final_number, NUMEROLOGY_MAPPING[5])
        
        calculation_steps = (
            f"Day: {day} → {day_reduced}, "
            f"Month: {month} → {month_reduced}, "
            f"Year: {year} → {year_reduced}, "
            f"Total: {day_reduced}+{month_reduced}+{year_reduced} = {total} → {final_number}"
        )
        
        return {
            "numerology_number": final_number,
            "personality_type": mapping["personality"],
            "element": mapping["element"],
            "calculation_steps": calculation_steps,
            "birthdate": birthdate_str
        }
        
    except Exception as e:
        print(f"Error calculating numerology: {e}")
        # Default fallback
        return {
            "numerology_number": 5,
            "personality_type": "Introvert",
            "element": "api",
            "calculation_steps": f"Error: {e}"
        }


# Test function
if __name__ == "__main__":
    # Test dengan contoh user
    test_cases = [
        "2012-12-19",  # Should be 9 = Ambivert AIR
        "1990-01-15",  # 15->6, 01->1, 1990->19->10->1 = 6+1+1=8 -> Extrovert LOGAM
        "1995-05-20",  # 20->2, 05->5, 1995->24->6 = 2+5+6=13->4 -> Extrovert TANAH
    ]
    
    for birthdate in test_cases:
        result = calculate_numerology_from_birthdate(birthdate)
        print(f"\nBirthdate: {birthdate}")
        print(f"Calculation: {result['calculation_steps']}")
        print(f"Number: {result['numerology_number']}")
        print(f"Result: {result['personality_type']} - {result['element'].upper()}")
