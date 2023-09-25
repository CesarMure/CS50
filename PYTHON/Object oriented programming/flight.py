class Flight():
    def __init__(self, capacity):
        #capacity of self is the maximum capacity
        self.capacity = capacity
        #empty passengers array
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        else:
            return True
        #appends a new passenger to the array
        self.passengers.append(name)

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"added {person} to flight successfully")
    else:
        print(f"no available seats for {person}")
 