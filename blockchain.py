from __future__ import annotations
from abc import ABC
import hashlib

class Mine(ABC):
    def mining():
        return "Minando componente"

class Chain(Mine):
    def __init__(self, difficulty: int) -> None:
        self._difficulty = difficulty
        self._blocks = []
        self._pool = [] 
        self.create_origin_block()
    
    def proof_work(self, block: Block) -> None:
        hash = hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        return block._hash.hexdigest() == hash.hexdigest() and int(hash.hexdigest(), 16) < 2 ** (256 - self._difficulty) and block.prev_block == self._blocks[-1]._hash

    def add_to_pool(self, data: Any) -> None:
        self._pool.append(data)

    def create_transaction(self, origin: str, destination: str, flight_duration: int) -> None:
        transaction = Transaction(origin, destination, flight_duration)
        self.add_to_pool(transaction)

    def create_origin_block(self) -> None:
        h = hashlib.sha256()
        h.update(''.encode('utf-8'))
        origin = Block("Origin", h)
        origin.mining(self._difficulty)
        self._blocks.append(origin)
    
    def mining(self) -> str:
        if len(self._pool) > 0:
            while len(self._pool) > 0:
                data = self._pool.pop()
                block = Block(data, self._blocks[-1]._hash)
                block.mining(self._difficulty)
                if(self.proof_work(block)):
                    self._blocks.append(block)
                    print("Blocked mined succesfully")
                else:
                    return "Invalid Block"
            return "Flights added to the chain"
        else: 
            return "There is nothing to mine"

    def print_chain(self):
        for block in self._blocks:
            print("Data:" , block._data, "Hash:", int(block._hash.hexdigest(), 16), "Previous Hash:", int(block.prev_block.hexdigest(), 16), "Nonce:", block._nonce)

    def save(self) -> Memento:
        return Memento(self._blocks)
    
    def restore(memento: Memento):
        self._blocks = memento.get_chain()

class Block(Mine):
    def __init__(self, data: Transaction, previous_hash: hashlib) -> None:
        self._hash = hashlib.sha256()
        self._nonce = 0
        self._data = data
        self.prev_block = previous_hash

    def mining(self, difficulty: int) -> None:
        self._hash.update(str(self).encode('utf-8'))
        while int(self._hash.hexdigest(), 16) > 2 ** (256 - difficulty):
            self._nonce += 1
            self._hash = hashlib.sha256()
            self._hash.update(str(self).encode('utf-8'))
        

    def __str__(self) -> str:
        return f"Data: {self._data} Nonce: {self._nonce} Previous:{self.prev_block.hexdigest()}"
    
class Transaction:
    def __init__(self, origin: str, destination: str, flight_duration: int) -> None:
        self.origin = origin
        self.destination = destination
        self.flight_duration = flight_duration

    def __str__(self) -> str:
        return f'{self.origin}:{self.destination}'

class Memento:
    def __init__(self, chain: Chain):
        self._chain = Chain
    
    def get_chain(self):
        return self._chain
            

