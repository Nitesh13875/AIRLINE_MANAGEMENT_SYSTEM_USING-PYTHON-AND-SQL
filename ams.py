import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kanishkajha@",
    database="AMS"
)
cursor = mydb.cursor()

def reserve_seat():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email address: ")
    flight_number = input("Enter the flight number: ")
    cursor.execute("SELECT id FROM flights WHERE flight_number = %s", (flight_number,))
    flight_id = cursor.fetchone()[0]
    cursor.execute("SELECT seat_number FROM passengers WHERE flight_id = %s", (flight_id,))
    taken_seats = [seat[0] for seat in cursor.fetchall()]
    available_seats = set([str(i) for i in range(1, 11)]) - set(taken_seats)
    if not available_seats:
        print("Sorry, there are no seats available for this flight.")
        return
    seat_number = input(f"Choose a seat from the following available seats: {', '.join(available_seats)} ")
    if seat_number not in available_seats:
        print("Sorry, the seat you chose is already taken.")
        return
    cursor.execute("INSERT INTO passengers (name, age, email, flight_id, seat_number) VALUES (%s, %s, %s, %s, %s)", (name, age, email, flight_id, seat_number))
    mydb.commit()
    print("Your seat has been reserved successfully.")

def crew_members():
    flight_id = input("Enter flight ID: ")
    cursor.execute("SELECT id, name, position, flight_id FROM crew_members WHERE flight_id = %s", (flight_id,))
    results = cursor.fetchall()
    if not results:
        print(f"No crew members found for flight {flight_id}.")
        return
    print("{:<15} {:<20} {:<20} {:<25}".format("id", "name", "position", "flight_id"))
    print("-" * 100)
    for result in results:
        print("{:<15} {:<20} {:<20} {:<25}".format(*result))

def payment_details():
    cursor.execute("SELECT id, payment_date, amount, payment_method, passenger_id FROM payment")
    results = cursor.fetchall()
    print("{:<15} {:<20} {:<20} {:<25}".format("id", "payment_date", "amount", "payment_method", "passenger_id"))
    print("-" * 100)
    for result in results:
        print("{:<15} {:<20} {:<20} {:<25}".format(*result))

def update_fine():
    passenger_id = input("Enter the passenger_id: ")
    new_fine_amount = float(input("Enter the fine amount: "))
    update_query = "UPDATE luggage SET fine = %s WHERE passenger_id = %s"
    values = (new_fine_amount, passenger_id)
    cursor.execute(update_query, values)
    mydb.commit()
    print(f"Updated fine amount for passenger {passenger_id} to {new_fine_amount}")

def flight_schedule():
    cursor.execute("SELECT flight_number, departure_airport, arrival_airport, DATE_FORMAT(departure_time, '%Y-%m-%d %I:%i %p'), DATE_FORMAT(arrival_time, '%Y-%m-%d %I:%i %p') FROM flights")
    results = cursor.fetchall()
    if not results:
        print("No flights found.")
        return
    print("{:<15} {:<20} {:<20} {:<25} {:<25}".format("Flight Number", "Departure Airport", "Arrival Airport", "Departure Time", "Arrival Time"))
    print("-" * 100)
    for result in results:
        print("{:<15} {:<20} {:<20} {:<25} {:<25}".format(*result))

def display_passengers():
    flight_number = input("Enter the flight number: ")
    cursor.execute("SELECT passengers.name, passengers.age, passengers.email, passengers.seat_number, passenger_info.food_preference, passenger_info.is_senior_citizen FROM passengers JOIN flights ON passengers.flight_id = flights.id LEFT JOIN passenger_info ON passengers.id = passenger_info.passenger_id WHERE flights.flight_number = %s", (flight_number,))
    results = cursor.fetchall()
    if not results:
        print("No passengers found for that flight.")
        return
    print("{:<20} {:<10} {:<30} {:<15} {:<20} {:<20}".format("|Name", "|Age", "|Email", "|Seat Number", "|Food Preference", "|Senior Citizen"))
    print("-" * 120)
    for result in results:
        print("{:<20} {:<10} {:<30} {:<15} {:<20} {:<20}".format(*result))

def user_ticket():
    email = input("Enter your email address: ")
    cursor.execute("SELECT passengers.id, passengers.name, passengers.age, flights.flight_number, flights.departure_airport, flights.arrival_airport, flights.departure_time, flights.arrival_time, passengers.seat_number FROM passengers JOIN flights ON passengers.flight_id = flights.id WHERE passengers.email = %s", (email,))
    result= cursor.fetchone()
    if not result:
        print("No ticket found with that email address.")
        return
    print("-" * 120)
    print("{:<20} {:<10} {:<30} {:<15} {:<20} {:<20}".format(*result))

while True:
    print("Airline Management System")
    print("1. Reserve Seat")
    print("2. User Ticket")
    print("3. Flight Schedule")
    print("4. Display Passengers")
    print("5. Update Luggage Fine")
    print("6. Crew Members")
    print("7. Payment Details")
    print("8. Exit Program")
    choice = input("Enter your choice: ")
    if choice == "1":
        reserve_seat()
    elif choice == "2":
        user_ticket()
    elif choice == "3":
        flight_schedule()
    elif choice == "4":
        display_passengers()
    elif choice == "5":
        update_fine()
    elif choice == "6":
        crew_members()
    elif choice == "7":
        payment_details()
    elif choice == "8":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
