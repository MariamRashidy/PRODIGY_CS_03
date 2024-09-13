import re

def check_password_strength(password):
    # Initialize variables to check criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    digit_criteria = re.search(r'[0-9]', password)
    special_char_criteria = re.search(r'[@#$%^&*()_+!]', password)
    
    # Calculate strength based on criteria met
    strength = 0
    feedback = []
    
    if length_criteria:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if uppercase_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")
    
    if lowercase_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")
    
    if digit_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one number.")
    
    if special_char_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one special character (e.g., @, #, !).")
    
    # Provide feedback based on the strength
    if strength == 5:
        feedback.append("Password is strong!")
    elif 3 <= strength < 5:
        feedback.append("Password is moderate, consider making it stronger.")
    else:
        feedback.append("Password is weak, please improve it.")
    
    return feedback

def main():
    password = input("Enter a password to check its strength: ")
    feedback = check_password_strength(password)
    
    print("\nPassword Strength Feedback:")
    for line in feedback:
        print(f"- {line}")

if __name__ == "__main__":
    main()
