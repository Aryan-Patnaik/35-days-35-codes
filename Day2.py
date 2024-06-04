# Define the block size for AES encryption
BLOCK_SIZE = 16

# Define a function to perform XOR operation on two bytes
def xor_bytes(byte1, byte2):
    return bytes(a ^ b for a, b in zip(byte1, byte2))

# Define a function to pad data to make its length a multiple of the block size
def pad_data(data):
    # Calculate the padding length required
    padding_length = BLOCK_SIZE - len(data) % BLOCK_SIZE
    # Create padding bytes using the padding length
    padding = bytes([padding_length] * padding_length)
    # Append padding to the data
    return data + padding

# Define a function to encrypt a single block using AES
def encrypt_block(block, key):
    # Perform XOR operation between the block and the key
    encrypted_block = xor_bytes(block, key)
    return encrypted_block

# Define a function to decrypt a single block using AES
def decrypt_block(encrypted_block, key):
    # Perform XOR operation between the encrypted block and the key
    decrypted_block = xor_bytes(encrypted_block, key)
    return decrypted_block

# Define a function to encrypt data using AES in ECB mode
def encrypt_data(data, key):
    # Pad the data to make its length a multiple of the block size
    padded_data = pad_data(data)
    # Initialize an empty byte string to store encrypted data
    encrypted_data = b''
    # Iterate over the padded data in blocks of the block size
    for i in range(0, len(padded_data), BLOCK_SIZE):
        # Extract a block of data
        block = padded_data[i:i+BLOCK_SIZE]
        # Encrypt the block using the key
        encrypted_block = encrypt_block(block, key)
        # Append the encrypted block to the encrypted data
        encrypted_data += encrypted_block
    return encrypted_data

# Define a function to decrypt data using AES in ECB mode
def decrypt_data(encrypted_data, key):
    # Initialize an empty byte string to store decrypted data
    decrypted_data = b''
    # Iterate over the encrypted data in blocks of the block size
    for i in range(0, len(encrypted_data), BLOCK_SIZE):
        # Extract a block of encrypted data
        encrypted_block = encrypted_data[i:i+BLOCK_SIZE]
        # Decrypt the block using the key
        decrypted_block = decrypt_block(encrypted_block, key)
        # Append the decrypted block to the decrypted data
        decrypted_data += decrypted_block
    return decrypted_data

# Set the password for encryption/decryption
password = 'secret_key_1234'

# Input data to be encrypted
data_to_encrypt = input("Enter your message: ")

# Encrypt the input data using the password as the key
encrypted_data = encrypt_data(data_to_encrypt.encode(), password.encode())

# Print the encrypted data
print("Encrypted data:", encrypted_data)

# Decrypt the encrypted data using the password as the key
decrypted_data = decrypt_data(encrypted_data, password.encode()).decode()

# Print the decrypted data
print("Decrypted data:", decrypted_data)
