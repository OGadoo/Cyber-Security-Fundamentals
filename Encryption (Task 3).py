import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def encrypt_dir(directory, key_file='key.bin', file_types=('.txt', '.docx', '.jpg')):
    key = get_random_bytes(32)
    with open(key_file, 'wb') as kf: kf.write(key)
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(file_types):
                with open(os.path.join(root, file), 'rb+') as f:
                    data, cipher = f.read(), AES.new(key, AES.MODE_CBC)
                    f.seek(0); f.write(cipher.iv + cipher.encrypt(pad(data, AES.block_size))); f.truncate()

if __name__ == "__main__":
    encrypt_dir(input("Enter directory to encrypt files: ").strip())
    print("Encryption complete. Key stored in 'key.bin'.") 