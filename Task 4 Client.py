import os
import requests
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher.iv + cipher.encrypt(pad(data, AES.block_size))

def send_file_to_server(file_path, server_url):
    try:
        key = get_random_bytes(32)
        encrypted_data = encrypt_file(file_path, key)

        # Save the encryption key securely
        with open("key.bin", "wb") as key_file:
            key_file.write(key)

        # Send the encrypted file to the server
        files = {'file': ('encrypted_file', encrypted_data)}
        response = requests.post(server_url, files=files)

        print(f"Server responded with: {response.text}")
    except PermissionError:
        print(f"Permission denied: Unable to access the file or folder '{file_path}'.")
    except FileNotFoundError:
        print(f"File not found: '{file_path}'. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the file path to encrypt and send: ").strip()
    if not os.path.exists(file_path):
        print("File does not exist. Please provide a valid file path.")
    else:
        server_url = "http://localhost:8000"
        send_file_to_server(file_path, server_url)