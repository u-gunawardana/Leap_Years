# Leap Years

Simple script to check which years in a range are leap years.

## Description
Reads two years (start and end) and prints whether each year in the range is a leap year.

## Requirements
- Python 3.8+

## Usage
Interactive:
```bash
python Leap_Years/leap_years.py
# then follow prompts for first and second year
```

Positional arguments (if implemented):
```bash
python Leap_Years/leap_years.py <first_year> <second_year>
```

## Examples
- Check 2000–2005:
```bash
python Leap_Years/leap_years.py 2000 2005
```

## Notes
- Avoid negative years; validate input before running or add input validation to the script.
- By convention, leap-year rule: divisible by 4 and not by 100, unless divisible by 400.
