from airport import Airport, City
from crew import Crew
from flight import Flight
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

    seat1 = Seat('A11')
    seat2 = Seat('A12')

    seat_list = [seat1, seat2]


    flight1 = Flight('National', airport1, airport2, datetime.now().strftime('%H:%M:%S'), datetime.now().strftime('%d/%m/%Y'), seat_list, crew_list)

    print(flight1.destination)

    # print(datetime.now().strftime('%d-%m-%Y'))
