from airport import Airport, City
from crew import Crew
from flight import Flight
from person_with_reservation import Passenger, Operator 
from reservation import Reservation
from seat import Seat

from datetime import datetime

if __name__ == '__main__':
    #1
    city1 = City('PDF', 'Brazil', 'RN')
    city2 = City('Patu', 'Brazil', 'RN')

    #2
    airport1 = Airport(city1, 3, "Foo's Airport")
    airport2 = Airport(city2, 3, 'Standard Airport')

    #3
    crew_member1 = Crew('Jessie', 'Pilot')
    crew_member2 = Crew('Mozilla', 'Co-pilot')
    crew_list = [crew_member1, crew_member2]

    #4
    seat_list = {
        'A11': Seat('A11'),
        'A12': Seat('A12'),
        'A13': Seat('A13'),
        'B11': Seat('B11'),
        'B12': Seat('B12'), 
        'B13': Seat('B13')
    }

    #5
    flight1 = Flight('National', airport1, airport2, datetime.now().time(), datetime.now().date(), seat_list, crew_list)

    """
        Cria dois passageiros, um operador e 3 requisições de reserva para bancos diferentes.
        O passageiro Carlos paga a primeira requisição e o operador Muriel cria a reserva.
    """

    #6 
    carlos_passenger = Passenger('Carlos')
    cristina_passenger = Passenger('Cristina')

    muriel_operator = Operator('Muriel', flight1)
    
    #7
    request1 = carlos_passenger.create(flight1, 'A11')
    request2 = cristina_passenger.create(flight1, 'A12')
    request3 = carlos_passenger.create(flight1, 'A13')

    #8 
    if carlos_passenger.pay(request1):
        muriel_operator.create(request1)
        reservation1 = Reservation(carlos_passenger, muriel_operator, flight1, seat_list['A11'])

    if cristina_passenger.pay(request2):
        muriel_operator.create(request2)
        reservation2 = Reservation(cristina_passenger, muriel_operator, flight1, seat_list['A13'])

    #10
    print('RESERVATIONS\n')
    print(reservation1)
    print()
    print(reservation2)

    print('REQUESTS\n')
    print(request3)

    #11
    print('\nPassenger cancels reservation request')
    cristina_passenger.cancel()

    print('Operator cancels reservation')
    muriel_operator.cancel('A12', reservation2)

    print('\nTrying to print a canceled reservation, throws exception: ')
    try:
        print(reservation2)

    except ValueError as e:
        print(f"\n==> {e}\n")

    #12
    freeSeats = flight1.freeSeats()
    flight1_crew = flight1.showCrew()

    print('AVAILABLE SEATS:')
    for seat in freeSeats:
        print(seat)

    print('\nCREW INFO:')
    for crew in flight1_crew:
        print(crew)
        print()

    print()




