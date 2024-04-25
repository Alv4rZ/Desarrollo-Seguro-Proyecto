from airport import Airport

benito_juarez = Airport('Benito', 'CDMX', 'Estado de mexico', 10)
miguel_hidalgo = Airport('Miguel', 'Guadalajara', 'Jalisco', 12)
vicente_guerrero = Airport('Vicente', 'Hidalgo', 'Hidalgo', 9)

benito_juarez.register_flight(benito_juarez, miguel_hidalgo, 221, 'Boing 767', 4)
miguel_hidalgo.register_flight(miguel_hidalgo, benito_juarez, 221, 'Boing 767', 4)

benito_juarez.register_flight(benito_juarez, miguel_hidalgo, 231, 'Boing 767', 4)
miguel_hidalgo.register_flight(miguel_hidalgo, benito_juarez, 231, 'Boing 767', 4)

benito_juarez.register_flight(benito_juarez, miguel_hidalgo, 551, 'Boing 767', 4)
miguel_hidalgo.register_flight(miguel_hidalgo, benito_juarez, 551, 'Boing 767', 4)

benito_juarez.register_flight(benito_juarez, vicente_guerrero, 443, 'Boing 767', 3)
vicente_guerrero.register_flight(vicente_guerrero, benito_juarez, 443, 'Boing 767', 3)

benito_juarez.get_all_flights()
benito_juarez.flight_arrived(551)
benito_juarez.flight_arrived(221)
benito_juarez.flight_arrived(443)
benito_juarez.get_all_flights()

benito_juarez.add_to_chain()
benito_juarez.secured_flights()
benito_juarez.get_all_flights()
