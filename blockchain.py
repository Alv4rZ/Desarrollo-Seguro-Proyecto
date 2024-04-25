from __future__ import annotations
from flight import Flight
import hashlib
import datetime
class Chain:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blocks = []
        self.pool = [] 
        self.create_origin_block()
    
    def proof_work(self, block):
        hash = hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        return block.hash.hexdigest() == hash.hexdigest() and int(hash.hexdigest(), 16) < 2 ** (256 - self.difficulty) and block.prev_block == self.blocks[-1].hash

    def add_to_pool(self, data):
        self.pool.append(data)

    def create_transaction(self, origin: str, destination: str, flight_duration: int, flight: Flight):
        transaction = Transaction(origin, destination, flight_duration, flight)
        self.add_to_pool(transaction)

    def create_origin_block(self) -> None:
        h = hashlib.sha256()
        h.update(''.encode('utf-8'))
        origin = Block("Origin", h)
        origin.mine(self.difficulty)
        self.blocks.append(origin)
    
    def mine(self) -> str:
        if len(self.pool) > 0:
            data = self.pool.pop()
            block = Block(data, self.blocks[-1].hash)
            block.mine(self.difficulty)
            self.add_to_chain(block)
            return "Blocked mined succesfully"
        else: 
            return "There is nothing to mine"

class Block:
    def __init__(self, data: Transaction, previous_hash: hashlib):
        self.hash = hashlib.sha256()
        self.nonce = 0
        self.data = data
        self.prev_block = previous_hash

    def mine(self, difficulty: int):
        self.hash.update(str(self).encode('utf-8'))
        while int(self.hash.hexdigest(), 16) > 2 ** (256 - difficulty):
            self.nonce += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode('utf-8'))
        

    def __str__(self):
        return f"Data: {self.data} Nonce: {self.nonce} Previous:{self.prev_block.hexdigest()}"
    


class Transaction:
    def __init__(self, origin: str, destination: str, flight_duration: int) -> None:
        self.origin = origin
        self.destination = destination
        self.flight_duration = flight_duration
        self.departure = datetime.datetime.now()

    def __str__(self) -> str:
        return f'{self.origin}:{self.destination}'
            

