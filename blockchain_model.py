import hashlib
import json
from time import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data  # Store data as a dictionary
        self.hash = hash

    def to_dict(self):
        return {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'data': self.data,
            'hash': self.hash
        }

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", time(), {"message": "Genesis Block"}, self.hash_block(0, "0", time(), {"message": "Genesis Block"}))
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def hash_block(self, index, previous_hash, timestamp, data):
        block_string = f'{index}{previous_hash}{timestamp}{json.dumps(data)}'
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_block(self, data):
        last_block = self.get_last_block()
        new_block = Block(
            len(self.chain), 
            last_block.hash, 
            time(), 
            data,  # Here data should be passed as a dictionary
            self.hash_block(len(self.chain), last_block.hash, time(), data)
        )
        self.chain.append(new_block)
        return new_block

    def verify_identity(self, identity):
        for block in self.chain:
            # Ensure block.data is a dictionary (which it should be after the change)
            if isinstance(block.data, dict) and block.data.get('identity') == identity:
                return True
        return False

