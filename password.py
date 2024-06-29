import random
import string

def generate_password(length):
    allcharacters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(allcharacters) for i in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    if password:
        print("Generated password : ", password)

if __name__ == "__main__":
    main()