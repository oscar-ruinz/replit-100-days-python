ContactInfo = {}

print("🌟Contact Card🌟\n")
ContactInfo["name"] = input("Input your name > ").strip().capitalize()
print()
ContactInfo["birth"] = input("Input your date of birth > ").strip()
print()
ContactInfo["phone"] = input("Input your telephone number > ").strip()
print()
ContactInfo["email"] = input("Input your email > ").strip()
print()
ContactInfo["address"] = input("Input your address > ").strip()
print("\n\n")
print(f"Hi {ContactInfo['name']}. Our dictionary says that were born on {ContactInfo['birth']}, we can call you on {ContactInfo['phone']}, email {ContactInfo['email']}, or write to {ContactInfo['address']}")