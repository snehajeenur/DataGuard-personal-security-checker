import re

def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return "Valid"
    else:
        return "Invalid"

def check_phone(phone):
    if phone.isdigit() and len(phone) == 10:
        return "Valid"
    else:
        return "Invalid"

def check_password(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[@#$%^&*]", password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3 or strength == 4:
        return "Medium"
    else:
        return "Strong"


email = input("Enter your email: ")
phone = input("Enter phone number: ")
password = input("Enter password: ")

print("\nEmail:", check_email(email))
print("Phone:", check_phone(phone))
print("Password strength:", check_password(password))