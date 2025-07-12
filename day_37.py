print("🌟Star Wars Name Generator🌟")

firstName = input("\nInput your first name > ").strip().lower()
lastName = input("\nInput your last name > ").strip().lower()
maidenName = input("\nInput your mother's maiden name > ").strip().lower()
cityBorn = input("\nInput the city where you were born > ").strip().lower()

swFirstName = str(firstName[:3] + lastName[:3]).capitalize()
swLastName = str(maidenName[:2] + cityBorn[-3:]).capitalize()

print(f"\nYour Star Wars name is {swFirstName} {swLastName}")
