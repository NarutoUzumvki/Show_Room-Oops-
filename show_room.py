class Customer :
    def __init__(self, name, phone_no):
        self.name = name
        self.phone_no = phone_no
        self.owned = []

    def show_owned(self):
        for owned in self.owned :
            print(self.name + " --", owned)
         

    def __str__(self):
        return self.owned + self.name + str(self.phone_no) 


class Vehicle :
    def __init__(self, name, mileage, price) :
        # self.vehicle = []
        self.name = name
        self.mileage = mileage
        self.price = price
        # self.vehicle.append(vehicle_name)
        # self.vehicle.append(mileage)
        # self.vehicle.append(price)


    def __str__(self):
        return self.name + " | " + str(self.mileage) + " | "  + str(self.price)

class Show_Room :
    def __init__(self):
        self.vehicles = []

    def add_to_show_room(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"{vehicle.name} has been added to the Show_room...")

    def remove_from_show_room(self, vehicle):
        self.vehicles.remove(vehicle)
        print(f"{vehicle.name} has been removed from the Show_room...\n")


    def view_show_room(self):
        print("Total vehicles Present in Show Room : ")
        for vehicle in self.vehicles :
            print(vehicle)

    def buy_vehicle(self, customer, vehicle):
        if vehicle in self.vehicles :
            purchase_proof = f"\nMr. {customer.name}... You have bought '{vehicle.name}' Whose Mileage is {vehicle.mileage} Kmph. and its Cost is Rs.{vehicle.price}. "
            print(purchase_proof)
            customer.owned.append(vehicle)

        else :
            print(f"\nSorry, Mr.{customer.name}.... {vehicle.name} is not present in Show Room.")


if __name__ == "__main__" :
    customer1 = Customer("Vijay", 7908412282)
    customer2 = Customer("Gojo", 9045682357)

    vehicle1 = Vehicle("Ntorq", 40, 120000)
    vehicle2 = Vehicle("Apache", 45, 210000)

    show_room = Show_Room()
    show_room.add_to_show_room(vehicle1)
    show_room.add_to_show_room(vehicle2)
    show_room.view_show_room()

    show_room.buy_vehicle(customer1, vehicle1)
    customer1.show_owned()

    show_room.remove_from_show_room(vehicle2)
    show_room.view_show_room()

    show_room.buy_vehicle(customer2, vehicle2)
    customer2.show_owned()

    show_room.add_to_show_room(vehicle2)
    show_room.view_show_room()

    show_room.buy_vehicle(customer1, vehicle2)
    customer1.show_owned()

    show_room.buy_vehicle(customer2, vehicle2)
    customer2.show_owned()