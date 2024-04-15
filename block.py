import hashlib
class Block:
    def __init__(self, data, previous_hash):
        self.hash = hashlib.sha256()
        self.nonce = 0
        self.data = data
        self.next_block = None
        self.prev_block = previous_hash

    def mine(self, difficulty):
        self.hash.update(str(self).encode('utf-8'))
        while int(self.hash.hexdigest(), 16) > 2 ** (256 - difficulty):
            self.nonce += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode('utf-8'))
        

    def __str__(self):
        return f"Data: {self.data} Nonce: {self.nonce} Previous:{self.prev_block.hexdigest()}"

    
