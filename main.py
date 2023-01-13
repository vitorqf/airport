from airport import Airport, City
from crew import Crew
from flight import Flight
from passenger import Passenger, Operator
from reservation import Reservation
from seat import Seat

from datetime import datetime

if __name__ == '__main__':
    city1 = City('PDF', 'Brazil', 'RN')
    city2 = City('Patu', 'Brazil', 'RN')

    airport1 = Airport(city1, 3, "Foo's Airport")
    airport2 = Airport(city2, 3, 'Standard Airport')

    crew_member1 = Crew('Jessie', 'Pilot')
    crew_member2 = Crew('Mozilla', 'Co-pilot')

    crew_list = [crew_member1, crew_member2]

    seat_list = {
        'A11': Seat('A11'),
        'A12': Seat('A12'),
        'A13': Seat('A13'),
        'B11': Seat('B11'),
        'B12': Seat('B12'),
        'B13': Seat('B13')
    }

    flight1 = Flight('National', airport1, airport2, datetime.now(), datetime.now(), seat_list, crew_list)

    carlos_passenger = Passenger('Carlos', flight1)
    muriel_operator = Operator('Muriel', flight1)

    muriel_operator.create(carlos_passenger, 'B11')
    reservation1 = Reservation(carlos_passenger, muriel_operator, flight1, seat_list['B11'])

    freeSeats = flight1.freeSeats()

    for seat in freeSeats:
        print(seat)


    print(reservation1)

    # reservation1 = Reservation(flight1)

    # print(reservation1.flight)

    

    # print(datetime.now().strftime('%d-%m-%Y'))

