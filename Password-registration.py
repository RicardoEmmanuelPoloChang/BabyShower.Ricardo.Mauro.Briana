#STEP1
import string
def generate_password():
    password = []
    while len(password) < 8:
        char = input("Enter a character of the password: ")
        if char.isalnum():
            password.append(char)
        else:
            print("Invalid character. Please enter only letters or numbers.")
    return ''.join(password)
#STEP2
if __name__ == "__main__":
    password = generate_password()
    print("Generated Password:", password)

