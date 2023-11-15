import os
import json
from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
def generate_key():
    return Fernet.generate_key()

# Encrypt the password using the key
def encrypt_password(key, password):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

# Decrypt the password using the key
def decrypt_password(key, encrypted_password):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password

# Save encrypted passwords to a JSON file
def save_passwords(accounts, key):
    encrypted_accounts = {}
    for account, password in accounts.items():
        encrypted_password = encrypt_password(key, password)
        encrypted_accounts[account] = encrypted_password

    with open('passwords.json', 'w') as file:
        json.dump(encrypted_accounts, file)

# Load encrypted passwords from the JSON file
def load_passwords(key):
    if not os.path.exists('passwords.json'):
        return {}
    with open('passwords.json', 'r') as file:
        encrypted_accounts = json.load(file)

    decrypted_accounts = {}
    for account, encrypted_password in encrypted_accounts.items():
        decrypted_password = decrypt_password(key, encrypted_password)
        decrypted_accounts[account] = decrypted_password

    return decrypted_accounts

# Main function to interact with the password manager
def password_manager():
    # Generate or load the encryption key
    if os.path.exists('key.key'):
        with open('key.key', 'rb') as key_file:
            key = key_file.read()
    else:
        key = generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)

    # Load existing passwords from the file
    accounts = load_passwords(key)

    while True:
        print("Password Manager")
        print("1. Add Account and Password")
        print("2. Retrieve Password")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            account = input("Enter account name: ")
            password = input("Enter password: ")
            accounts[account] = password
            save_passwords(accounts, key)
            print("Account and Password added successfully!")

        elif choice == '2':
            account = input("Enter account name: ")
            if account in accounts:
                password = accounts[account]
                print(f"Password for '{account}': {password}")
            else:
                print("Account not found!")

        elif choice == '3':
            print("Exiting Password Manager...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    password_manager()
