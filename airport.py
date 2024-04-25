from __future__ import annotations
from blockchain import Chain
from flight import Flight
class Airport:
    def __init__(self, name: str, city: str, state: str, difficulty: int) -> None:
        self.name = name
        self.city = city
        self.state = state
        self.chain = Chain(difficulty)

    def register_flight(self, flight: Flight, origin: str, destination: str):
        pass
        
    
    def __str__(self) -> str:
        return f'Airport: {self.name} in city: {self.city} in state: {self.state}'
