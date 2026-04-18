# Password Complexity Checker
import re

def check_password_strength(password):
    feedback = []
    strength = 0

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for digits
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    # Check for special characters
    if re.search(r'[^A-Za-z0-9]', password):
        strength += 1
    else:
        feedback.append("Add at least one special character.")

    # Provide overall feedback
    if strength == 5:
        return "Strong password!", feedback
    elif strength >= 3:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    result, suggestions = check_password_strength(pwd)
    print(f"Password Strength: {result}")
    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print(f"- {s}")
