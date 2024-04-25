from __future__ import annotations
from blockchain import Chain
from flight import Flight
class Airport:
    def __init__(self, name: str, city: str, state: str, difficulty: int) -> None:
        self.name = name
        self.city = city
        self.state = state
        self._chain = Chain(difficulty)
        self._history = []
        self._arrived = []
        self._flying = {}

    def register_flight(self, origin: Airport, destination: Airport, number: int, plane_type: str, duration: int) -> str:
        flight = Flight(number, plane_type, duration, origin, destination)
        self._flying[flight._number] = flight
        return f'Flight registered succesfully'

    def get_all_flights(self) -> None:
        print(20*"#")
        for ids in self._flying:
            print(self._flying[ids]._id, "Destination:", self._flying[ids].destination.name, "Origin:", self._flying[ids].origin.name, "Number:", self._flying[ids]._number, "Landed:", self._flying[ids]._landed)
        print(20*"#")

    def flight_arrived(self, number: int) -> str:
        self._flying[number].successful_landing()
        return f'Flight {number} arrived succesfully'
        
    def add_to_chain(self) -> None:
        for ids in self._flying:
            if self._flying[ids]._landed == True:
                self._chain.create_transaction(self._flying[ids].origin.name, self._flying[ids].destination.name, self._flying[ids].duration)
                self._arrived.append(self._flying[ids]._number)
        self._chain.mining()
        memento = self._chain.save()
        self._history.append(memento)
        for number in self._arrived:
            del self._flying[number]
        self._arrived = []
    
    def cancel(self):
        self._history.pop()
        memento = self._history[-1]
        self._chain.restore(memento)
    
    def secured_flights(self):
        self._chain.print_chain()

    def __str__(self) -> str:
        return f'Airport: {self.name} in city: {self.city} in state: {self.state}'

