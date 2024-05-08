# -*- coding: utf-8 -*-
import unittest
from flight import Flight

class TestFlight(unittest.TestCase):

    def test_successful_landing(self):
        flight = Flight(123, 'Boeing 747', 240, 'Airport A', 'Airport B')
        flight.successful_landing()
        self.assertTrue(flight._landed)

    def test_copy(self):
        flight = Flight(123, 'Boeing 747', 240, 'Airport A', 'Airport B')
        flight_copy = flight.__copy__()
        self.assertNotEqual(flight, flight_copy)
        self.assertEqual(flight._id, flight_copy._id)
        self.assertEqual(flight._number, flight_copy._number)
        self.assertEqual(flight.plane_type, flight_copy.plane_type)
        self.assertEqual(flight.duration, flight_copy.duration)
        self.assertEqual(flight.origin, flight_copy.origin)
        self.assertEqual(flight.destination, flight_copy.destination)
        self.assertEqual(flight._landed, flight_copy._landed)

    def test_str(self):
        flight = Flight(123, 'Boeing 747', 240, 'Airport A', 'Airport B')
        self.assertEqual(str(flight), 'Vuelo número: 123, Tipo de avión: Boeing 747, Duración: 240 minutos, Aterrizado: No')

if __name__ == '__main__':
    unittest.main()
