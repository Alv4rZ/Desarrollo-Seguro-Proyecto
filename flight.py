from __future__ import annotations
import uuid

class Flight:
    def __init__(self, number: int, plane_type: str, duration: int, origin: str, destination: str) -> None:
        self._id = uuid.uuid4()
        self._number = number
        self.plane_type = plane_type
        self.duration = duration
        self.origin = origin
        self.destination = destination
        self._landed = False
    
    def successful_landing(self) -> None:
        self._landed = True
    
    def __copy__(self):
        return Flight(self._id, self._number, self.plane_type, self.duration, self.origin, self.destination, self._landed)

    def __str__(self) -> str:
        return f'Flight number: {self._number}, plane type: {self.plane_type}, duration: {self.duration}, landed: {self._landed}'
     

    
        