def calculate_atr(years_of_experience, age):
    """
    Calculates the Annual Tax Revenue (ATR) based on years of experience and age.

    Args:
        years_of_experience (int): The number of years of work experience.
        age (int): The age of the staff member.

    Returns:
        float: The calculated Annual Tax Revenue (ATR).
    """
    if years_of_experience > 25 and age >= 55:
        atr = 5600000.0
    elif years_of_experience > 20 and age >= 45:
        atr = 4480000.0
    elif years_of_experience > 10 and age >= 35:
        atr = 1500000.0
    else:
        atr = 550000.0
    return atr

# Get input from the user
try:
    experience = int(input("Enter the staff's years of experience: "))
    age = int(input("Enter the staff's age: "))

    # Calculate the ATR
    annual_tax_revenue = calculate_atr(experience, age)

    # Display the result
    print(f"\nThe Annual Tax Revenue (ATR) for this staff member is: N{annual_tax_revenue:,.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for years of experience and age.")