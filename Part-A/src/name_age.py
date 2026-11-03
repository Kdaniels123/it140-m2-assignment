"""
Simple program that asks the user for their name and age,
then calculates and displays the year they were born.
Assumes the user has already had their birthday this year.
"""

from datetime import datetime

# Get user input
name = input("What is your name? ")
age = int(input("How old are you? "))

# Calculate birth year using the current year
current_year = datetime.now().year
birth_year = current_year - age

# Display the result
print(f"Hello {name}! You were born in {birth_year}.")
