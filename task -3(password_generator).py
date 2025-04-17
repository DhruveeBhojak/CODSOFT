import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 for complexity."
    
    # Characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    password = generate_password(length)
    print(f"\nYour generated password is:\n👉 {password}")

if __name__ == "__main__":
    main()
