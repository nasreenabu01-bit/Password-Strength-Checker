print("================================")
print("     PASSWORD STRENGTH CHECKER")
print("================================")

password = input("Enter your password: ")

common_passwords = ["123456", "password", "qwerty", "abc123", "admin"]

score = 0

if len(password) >= 8:
    print("✓ Password length is good.")
    score += 1
else:
    print("✗ Password should be at least 8 characters long.")

if any(char.isupper() for char in password):
    print("✓ Contains an uppercase letter.")
    score += 1
else:
    print("✗ Should contain an uppercase letter.")

if any(char.islower() for char in password):
    print("✓ Contains a lowercase letter.")
    score += 1
else:
    print("✗ Should contain a lowercase letter.")

if any(char.isdigit() for char in password):
    print("✓ Contains a number.")
    score += 1
else:
    print("✗ Should contain a number.")

if any(not char.isalnum() for char in password):
    print("✓ Contains a special character.")
    score += 1
else:
    print("✗ Should contain a special character.")

if password.lower() in common_passwords:
    print("⚠ Warning: This is a common password.")
    score = 0

if len(set(password)) < len(password) / 2:
    print("⚠ Warning: Password contains many repeated characters.")

sequences = ["123", "456", "789", "abc", "xyz"]

for sequence in sequences:
    if sequence in password.lower():
        print("⚠ Warning: Password contains a predictable sequence.")
        break

print("--------------------------------")
print("Password score:", score, "/ 5")

if score <= 2:
    print("Password strength: Weak")
elif score <= 4:
    print("Password strength: Medium")
else:
    print("Password strength: Strong")

print("--------------------------------")