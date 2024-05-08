# -*- coding: utf-8 -*-
from __future__ import annotations
from abc import ABC
import hashlib


class Mine(ABC):
    """
    Clase abstracta que representa la acción de minería para una cadena de bloques.
    """

    def mining():
        """
        Método estático que representa el proceso de minería.
        Devuelve una cadena de texto para indicar que se está minando.
        """
        return 'Minando componente'


class Chain(Mine):
    """
    Patrón Estructural Facade
    Clase que representa la cadena de bloques.
    Gestiona la creación, adición y validación de bloques.
    """

    def __init__(self, difficulty: int) -> None:
        """
        Inicializa la cadena de bloques con la dificultad especificada.

        Args:
            difficulty (int): El nivel de dificultad para la minería de bloques.
        """
        self._difficulty = difficulty
        self._blocks = []
        self._pool = []  # Pool de transacciones por confirmar
        self.create_origin_block()  # Crea el bloque génesis

    def proof_work(self, block: Block) -> bool:
        """
        Realiza la validación del trabajo para un bloque.

        Args:
            block (Block): El bloque a verificar.

        Returns:
            bool: True si el bloque cumple con las condiciones de la prueba de trabajo, False en caso contrario.
        """
        hash = hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        return (
            block._hash.hexdigest() == hash.hexdigest()
            and int(block._hash.hexdigest(), 16) < 2 ** (256 - self._difficulty)
            and block.prev_block == self._blocks[-1]._hash
        )

    def add_to_pool(self, data) -> None:
        """
        Agrega datos a la pool de transacciones.

        Args:
            data: Información para agregar a la pool.
        """
        self._pool.append(data)

    def create_transaction(self, origin: str, destination: str, flight_duration: int) -> None:
        """
        Crea una transacción y la añade a la pool.

        Args:
            origin (str): Origen del vuelo.
            destination (str): Destino del vuelo.
            flight_duration (int): Duración del vuelo en minutos.
        """
        transaction = Transaction(origin, destination, flight_duration)
        self.add_to_pool(transaction)

    def create_origin_block(self) -> None:
        """
        Crea el bloque de origen (génesis) para la cadena de bloques.
        """
        h = hashlib.sha256()
        h.update(''.encode('utf-8'))
        origin = Block('Origin', h)
        origin.mining(self._difficulty)
        self._blocks.append(origin)

    def mining(self) -> str:
        """
        Realiza el proceso de minería y agrega bloques a la cadena si se validan correctamente.

        Returns:
            str: Mensaje indicando el estado del proceso de minería.
        """
        if len(self._pool) > 0:
            while len(self._pool) > 0:
                data = self._pool.pop()
                block = Block(data, self._blocks[-1]._hash)
                block.mining(self._difficulty)
                if self.proof_work(block):
                    self._blocks.append(block)
                    print('Bloque minado con éxito')
                else:
                    return 'Bloque inválido'
            return 'Vuelos agregados a la cadena'
        else:
            return 'No hay nada para minar'

    def print_chain(self) -> None:
        """
        Imprime la cadena de bloques en formato legible.
        """
        for block in self._blocks:
            print(
                'Datos:', block._data,
                'Hash:', int(block._hash.hexdigest(), 16),
                'Hash anterior:', int(block.prev_block.hexdigest(), 16),
                'Nonce:', block._nonce,
            )

    def save(self) -> Memento:
        """
        Guarda el estado actual de la cadena en un objeto Memento.

        Returns:
            Memento: El estado actual de la cadena.
        """
        return Memento(self._blocks)

    def restore(self, memento: Memento) -> None:
        """
        Restaura la cadena de bloques desde un objeto Memento.

        Args:
            memento (Memento): El objeto Memento para restaurar.
        """
        self._blocks = memento.get_chain()


class Block(Mine):
    """
    Clase que representa un bloque en la cadena de bloques.
    """

    def __init__(self, data: Transaction, previous_hash: hashlib) -> None:
        """
        Inicializa un bloque con datos y el hash del bloque anterior.

        Args:
            data (Transaction): Datos de la transacción en el bloque.
            previous_hash (hashlib): Hash del bloque anterior.
        """
        self._hash = hashlib.sha256()
        self._nonce = 0
        self._data = data
        self.prev_block = previous_hash

    def mining(self, difficulty: int) -> None:
        """
        Realiza el proceso de minería para el bloque.

        Args:
            difficulty (int): El nivel de dificultad para la minería.
        """
        self._hash.update(str(self).encode('utf-8'))
        while int(str(self._hash.hexdigest()), 16) > 2 ** (256 - difficulty):
            self._nonce += 1
            self._hash = hashlib.sha256()
            self._hash.update(str(self).encode('utf-8'))

    def __str__(self) -> str:
        """
        Representación de cadena de texto para el bloque.

        Returns:
            str: Descripción del bloque con sus datos y estado.
        """
        return f'Datos: {self._data}, Nonce: {self._nonce}, Anterior: {self.prev_block}'

class Transaction:
    """
    Clase que representa una transacción en la cadena de bloques.
    """

    def __init__(self, origin: str, destination: str, flight_duration: int) -> None:
        """
        Inicializa una transacción con origen, destino y duración del vuelo.

        Args:
            origin (str): Origen del vuelo.
            destination (str): Destino del vuelo.
            flight_duration (int): Duración del vuelo en minutos.
        """
        self.origin = origin
        self.destination = destination
        self.flight_duration = flight_duration

    def __str__(self) -> str:
        """
        Representación de cadena de texto para la transacción.

        Returns:
            str: Descripción de la transacción con origen y destino.
        """
        return f'{self.origin}:{self.destination}'


class Memento:
    """
    Patrón de comportamiento Memento
    Clase que representa un memento para guardar el estado de la cadena de bloques.
    """

    def __init__(self, chain: Chain):
        """
        Inicializa el memento con el estado actual de la cadena de bloques.

        Args:
            chain (Chain): La cadena de bloques para guardar en el memento.
        """
        self._chain = chain

    def get_chain(self):
        """
        Obtiene el estado actual de la cadena de bloques almacenado en el memento.

        Returns:
            list: Lista de bloques que componen la cadena de bloques.
        """
        return self._chain