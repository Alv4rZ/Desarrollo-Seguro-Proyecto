# -*- coding: utf-8 -*-
import unittest
from unittest.mock import MagicMock
from airport import Airport, Flight
from blockchain import Chain, Memento

class TestAirport(unittest.TestCase):

    def test_register_flight(self):
        airport = Airport('Airport A', 'City A', 'State A', 4)
        origin = Airport('Airport B', 'City B', 'State B', 4)
        destination = Airport('Airport C', 'City C', 'State C', 4)
        result = airport.register_flight(origin, destination, 123, 'Plane Type', 120)
        self.assertEqual(result, 'Vuelo registrado con éxito')

    def test_flight_arrived(self):
        airport = Airport('Airport A', 'City A', 'State A', 4)
        flight_mock = MagicMock()
        flight_mock._number = 123
        flight_mock.successful_landing.return_value = None
        airport._flying = {123: flight_mock}
        result = airport.flight_arrived(123)
        self.assertEqual(result, 'Vuelo 123 llegó con éxito')

    def test_add_to_chain(self):
        airport1 = Airport('Airport A', 'City A', 'State A', 4)
        airport2 = Airport('Airport B', 'City B', 'State B', 4)
        airport1.register_flight(airport1, airport2, 123, 'j', 3)
        airport1.register_flight(airport1,airport2, 456, 'j', 3)
        airport1._flying[123]._landed = True
        airport1._flying[456]._landed = False
        chain_mock = MagicMock()
        chain_mock.create_transaction.return_value = None
        chain_mock.mining.return_value = None
        chain_mock.save.return_value = Memento(None)
        airport1._chain = chain_mock
        airport1.add_to_chain()
        chain_mock.mining.assert_called_once()
        chain_mock.save.assert_called_once()

    def test_secured_flights(self):
        airport = Airport('Airport A', 'City A', 'State A', 4)
        chain_mock = MagicMock()
        chain_mock.print_chain.return_value = None
        airport._chain = chain_mock
        airport.secured_flights()
        chain_mock.print_chain.assert_called_once()