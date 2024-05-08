# -*- coding: utf-8 -*-
from __future__ import annotations
from blockchain import Chain
from flight import Flight


class Airport:
    """
    Clase que representa un aeropuerto y gestiona sus vuelos y cadena de bloques.
    """

    def __init__(self, name: str, city: str, state: str, difficulty: int) -> None:
        """
        Inicializa un aeropuerto con su información y configuración de cadena de bloques.

        Args:
            name (str): Nombre del aeropuerto.
            city (str): Ciudad donde se encuentra el aeropuerto.
            state (str): Estado donde se encuentra el aeropuerto.
            difficulty (int): Dificultad para la minería en la cadena de bloques.
        """
        self.name = name
        self.city = city
        self.state = state
        self._chain = Chain(difficulty)  # Cadena de bloques asociada al aeropuerto
        self._history = []  # Historial de cambios en la cadena de bloques
        self._arrived = []  # Vuelos que han llegado
        self._flying = {}  # Vuelos activos

    def register_flight(self, origin: Airport, destination: Airport, number: int, plane_type: str, duration: int) -> str:
        """
        Registra un vuelo desde un aeropuerto origen a un aeropuerto destino.

        Args:
            origin (Airport): Aeropuerto de origen.
            destination (Airport): Aeropuerto de destino.
            number (int): Número del vuelo.
            plane_type (str): Tipo de avión.
            duration (int): Duración del vuelo en minutos.

        Returns:
            str: Mensaje confirmando el registro del vuelo.
        """
        flight = Flight(number, plane_type, duration, origin, destination)
        self._flying[flight._number] = flight
        return 'Vuelo registrado con éxito'

    def get_all_flights(self) -> None:
        """
        Imprime información sobre todos los vuelos registrados y activos.
        """
        print('#' * 20)
        for ids in self._flying:
            print(
                f'Vuelo ID: {self._flying[ids]._id}, '
                f'Destino: {self._flying[ids].destination.name}, '
                f'Origen: {self._flying[ids].origin.name}, '
                f'Número: {self._flying[ids]._number}, '
                f"Atterrizaje: {'Sí' if self._flying[ids]._landed else 'No'}"
            )
        print('#' * 20)

    def flight_arrived(self, number: int) -> str:
        """
        Marca un vuelo como llegado al aeropuerto.

        Args:
            number (int): Número del vuelo que ha llegado.

        Returns:
            str: Mensaje confirmando el aterrizaje del vuelo.
        """
        self._flying[number].successful_landing()
        return f'Vuelo {number} llegó con éxito'

    def add_to_chain(self) -> None:
        """
        Agrega vuelos aterrizados a la cadena de bloques y realiza el proceso de minería.
        """
        for ids in self._flying:
            if self._flying[ids]._landed:
                self._chain.create_transaction(
                    self._flying[ids].origin.name,
                    self._flying[ids].destination.name,
                    self._flying[ids].duration
                )
                self._arrived.append(self._flying[ids]._number)
        self._chain.mining()
        memento = self._chain.save()  # Guarda el estado de la cadena
        self._history.append(memento)  # Guarda el memento en el historial
        for number in self._arrived:
            del self._flying[number]
        self._arrived = []

    def cancel(self) -> None:
        """
        Cancela la última operación de la cadena de bloques y restaura al estado anterior.
        """
        self._history.pop()  # Elimina el último memento
        memento = self._history[-1]  # Obtiene el último memento
        self._chain.restore(memento)  # Restaura la cadena de bloques

    def secured_flights(self) -> None:
        """
        Imprime la cadena de bloques para mostrar los vuelos asegurados.
        """
        self._chain.print_chain()

    def __str__(self) -> str:
        """
        Representación de cadena de texto para el aeropuerto.

        Returns:
            str: Descripción del aeropuerto.
        """
        return f'Aeropuerto: {self.name}, Ciudad: {self.city}, Estado: {self.state}'
