from airport import Airport

benito_juarez = Airport('Benito', 'CDMX', 'Estado de mexico', 5)
miguel_hidalgo = Airport('Miguel', 'Guadalajara', 'Jalisco', 6)
vicente_guerrero = Airport('Vicente', 'Hidalgo', 'Hidalgo', 7)

benito_juarez.register_flight(benito_juarez, miguel_hidalgo, 221, 'Boing 767', 4)
benito_juarez.register_flight(benito_juarez, miguel_hidalgo, 231, 'Boing 767', 4)
benito_juarez.register_flight(benito_juarez, miguel_hidalgo, 551, 'Boing 767', 4)
benito_juarez.register_flight(benito_juarez, vicente_guerrero, 443, 'Boing 767', 4)
benito_juarez.get_all_flights()
benito_juarez.flight_arrived(551)
benito_juarez.flight_arrived(221)
benito_juarez.flight_arrived(443)
benito_juarez.get_all_flights()

benito_juarez.add_to_chain()
benito_juarez.secured_flights()
