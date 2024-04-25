from __future__ import annotations
from blockchain import Chain
import uuid

class Flight:
    def __init__(self, number: int, plane_type: str, duration: int) -> None:
        self.id = uuid.uuid4()
        self.number = number
        self.plane_type = plane_type
        self.duration = duration
        self.landed = False
    
    def succesful_landing(self):
        self.landed = True

    @property
    def uuid(self):
        return self.uuid

    def __str__(self) -> str:
        return f'Flight number: {self.number}, plane type: {self.plane_type}, duration: {self.duration}, landed: {self.landed}'
     

    
        