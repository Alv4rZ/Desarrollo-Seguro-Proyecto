# -*- coding: utf-8 -*-
from __future__ import annotations
import uuid


class Flight:
    """
    Clase que representa un vuelo entre aeropuertos.
    """

    def __init__(self, number: int, plane_type: str, duration: int, origin: str, destination: str) -> None:
        """
        Inicializa un vuelo con información básica.

        Args:
            number (int): Número del vuelo.
            plane_type (str): Tipo de avión.
            duration (int): Duración del vuelo en minutos.
            origin (str): Aeropuerto de origen.
            destination (str): Aeropuerto de destino.
        """
        self._id = uuid.uuid4()  # Identificador único para el vuelo
        self._number = number
        self.plane_type = plane_type
        self.duration = duration
        self.origin = origin
        self.destination = destination
        self._landed = False  # Indica si el vuelo ha aterrizado

    def successful_landing(self) -> None:
        """
        Marca el vuelo como aterrizado.
        """
        self._landed = True

    def __copy__(self) -> Flight:
        """
        Patrón creacional Prototype.
        Crea una copia del vuelo.

        Returns:
            Flight: Una copia del vuelo actual.
        """
        return Flight(self._number, self.plane_type, self.duration, self.origin, self.destination)

    def __str__(self) -> str:
        """
        Representación de cadena de texto para el vuelo.

        Returns:
            str: Descripción del vuelo con información relevante.
        """
        return f"Vuelo número: {self._number}, Tipo de avión: {self.plane_type}, Duración: {self.duration} minutos, Aterrizado: {'Sí' if self._landed else 'No'}"
