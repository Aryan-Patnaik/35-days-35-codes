import hashlib  # Importing the hashlib library for hashing functions
import time  # Importing the time library to work with timestamps
from ecdsa import SigningKey, NIST384p, BadSignatureError  # Importing ECDSA for cryptographic signing and verifying

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        # Initialize a new block with the given attributes
        self.index = index  # Index of the block in the chain
        self.previous_hash = previous_hash  # Hash of the previous block in the chain
        self.timestamp = timestamp  # Timestamp of the block creation
        self.data = data  # Data contained in the block
        self.nonce = nonce  # Nonce value used for the proof of work
        self.hash = self.calculate_hash()  # Calculate the hash of the block

    def calculate_hash(self):
        # Calculate the hash of the block based on its contents
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()  # Return the SHA-256 hash of the block string

    def __str__(self):
        # Return a string representation of the block
        return f"Block(index: {self.index}, hash: {self.hash}, previous_hash: {self.previous_hash}, timestamp: {self.timestamp}, data: {self.data}, nonce: {self.nonce})"

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Create the blockchain with the genesis block

    def create_genesis_block(self):
        # Create the genesis block (the first block in the blockchain)
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        # Get the latest block in the blockchain
        return self.chain[-1]

    def add_block(self, new_block):
        # Add a new block to the blockchain
        new_block.previous_hash = self.get_latest_block().hash  # Set the previous hash of the new block to the hash of the latest block
        new_block.hash = new_block.calculate_hash()  # Calculate the hash of the new block
        self.chain.append(new_block)  # Append the new block to the chain

    def is_chain_valid(self):
        # Validate the blockchain
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]  # Current block in the chain
            previous_block = self.chain[i - 1]  # Previous block in the chain

            if current_block.hash != current_block.calculate_hash():  # Check if the hash of the current block is correct
                return False
            if current_block.previous_hash != previous_block.hash:  # Check if the previous hash of the current block matches the hash of the previous block
                return False
        return True  # Return True if the blockchain is valid

class Wallet:
    def __init__(self):
        self.private_key = SigningKey.generate(curve=NIST384p)  # Generate a new private key using ECDSA
        self.public_key = self.private_key.get_verifying_key()  # Get the public key corresponding to the private key

    def sign_data(self, data):
        # Sign the given data using the private key
        return self.private_key.sign(data.encode())

    def verify_signature(self, data, signature):
        # Verify the given signature for the data using the public key
        try:
            return self.public_key.verify(signature, data.encode())
        except BadSignatureError:
            return False  # Return False if the signature is invalid

blockchain = Blockchain()  # Create a new blockchain

blockchain.add_block(Block(1, blockchain.get_latest_block().hash, time.time(), "Block 1 Data"))  # Add the first block to the blockchain
blockchain.add_block(Block(2, blockchain.get_latest_block().hash, time.time(), "Block 2 Data"))  # Add the second block to the blockchain

print("Is blockchain valid?", blockchain.is_chain_valid())  # Check if the blockchain is valid

for block in blockchain.chain:
    print(block)  # Print each block in the blockchain

wallet = Wallet()  # Create a new wallet
data = "Some important data"  # Data to be signed
signature = wallet.sign_data(data)  # Sign the data using the wallet's private key

print("Signature valid?", wallet.verify_signature(data, signature))  # Verify the signature
print("Signature invalid?", wallet.verify_signature(data, b"fake_signature"))  # Verify a fake signature
