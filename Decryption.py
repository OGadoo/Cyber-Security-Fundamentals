import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_dir(directory, key_file='key.bin', file_types=('.txt', '.docx', '.jpg')):
    if not os.path.exists(key_file):
        print(f"Key file '{key_file}' not found.")
        return
    key = open(key_file, 'rb').read()
    
    # Create a decrypted folder
    decrypted_folder = os.path.join(directory, 'decrypted_files')
    os.makedirs(decrypted_folder, exist_ok=True)

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(file_types):
                with open(os.path.join(root, file), 'rb') as f:
                    iv, ciphertext = f.read(16), f.read()
                    try:
                        decrypted = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext), AES.block_size)
                        
                        # Save the decrypted file in decrypted_files folder
                        decrypted_filename = file.replace('.enc', '')  # remove .enc if exists
                        decrypted_path = os.path.join(decrypted_folder, decrypted_filename)
                        with open(decrypted_path, 'wb') as df:
                            df.write(decrypted)
                        
                        print(f"Decrypted and saved: {decrypted_filename}")
                    
                    except ValueError:
                        print(f"Failed to decrypt: {file}")

if __name__ == "__main__":
    decrypt_dir(input("Enter directory to decrypt files: ").strip())
    print("Decryption complete.")