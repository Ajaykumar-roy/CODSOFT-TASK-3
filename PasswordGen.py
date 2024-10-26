import random
import string

# Function to generate a random password
def generate_password(length, use_uppercase, use_digits, use_special):
    characters = string.ascii_lowercase  # Start with lowercase letters
    
    if use_uppercase:
        characters += string.ascii_uppercase  # Add uppercase letters if requested
    if use_digits:
        characters += string.digits  # Add digits if requested
    if use_special:
        characters += string.punctuation  # Add special characters if requested

    if length < 1:
        return "Error: Password length must be at least 1."
    
    # Generate the random password using the specified character set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to get user input for password criteria
def password_generator():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError: 
        print("Invalid input. Please enter a numeric value for the length.")
        return
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate the password
    password = generate_password(length, use_uppercase, use_digits, use_special)
    
    # Display the generated password
    print(f"\nGenerated Password: {password}")

# Run the password generator
if __name__ == "__main__":
    password_generator()
