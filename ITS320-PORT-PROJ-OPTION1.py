class Automobile:
    # This will initialize the variables that are used to determine individual automobiles
    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    # An example of toString (Java) - how the values will be returned to the user and stored within the
    # inventory array
    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color}), Mileage: {self.mileage}"

    # Setter / update function - this will fill / update the values of each automobile
    def update(self, make = None, model = None, color = None, year = None, mileage = None):
        if make:
            self.make = make
        if model:
            self.model = model
        if color:
            self.color = color
        if year:
            self.year = year
        if mileage:
            self.mileage = mileage

class DealershipInventory:
    # Initializing the inventory array
    def __init__(self):
        self.inventory = []

    # How vehicles are added to the inventory array
    def add_vehicle(self, vehicle):
        self.inventory.append(vehicle)

    # How vehicles are removed from the inventory array
    def remove_vehicle(self, index):
        if 0 <= index < len(self.inventory):
            self.inventory.pop(index)
        # Failsafe, if the index is incorrect or null
        else:
            print("Invalid index. Vehicle not found.")

    # How the user tells the program to update vehicles, how the vehicle is chosen via index
    def update_vehicle(self, index, make = None, model = None, color = None, year = None, mileage = None):
        if 0 <= index < len(self.inventory):
            self.inventory[index].update(make, model, color, year, mileage)
        # Failsafe, if the index is incorrect or null
        else:
            print("Invalid index. Vehicle not found.")

    # Function used to display the inventory to the user, will loop through and call the __str__ method
    # for each individual vehicle
    def display_inventory(self):
        for i, vehicle in enumerate(self.inventory):
            print(f"{i}: {vehicle}")

    # Function used to save current inventory to external file
    def save_inventory_to_file(self, filename):
        with open(filename, 'w') as file:
            for vehicle in self.inventory:
                file.write(str(vehicle) + '\n')

def main():
    # Calling dealership inventory class
    inventory = DealershipInventory()

    # Providing user options
    while True:
        print("\nDealership Inventory Management System")
        print("1. Add a new vehicle")
        print("2. Remove a vehicle")
        print("3. Update vehicle attributes")
        print("4. Display inventory")
        print("5. Save inventory to file")
        print("6. Exit")

        choice = input("Enter your choice: ")

        # Cases for all six options given to the user
        if choice == '1': # If the user wants to add a new vehicle
            make = input("Enter make: ")
            model = input("Enter model: ")
            color = input("Enter color: ")
            year = int(input("Enter year: "))
            mileage = int(input("Enter mileage: "))
            vehicle = Automobile(make, model, color, year, mileage)
            inventory.add_vehicle(vehicle)
        elif choice == '2': # If the user wants to remove a vehicle
            index = int(input("Enter index of vehicle to remove: "))
            inventory.remove_vehicle(index)
        elif choice == '3': # If the user wants to update an already existing vehicle
            index = int(input("Enter index of vehicle to update: "))
            make = input("Enter new make (leave blank to keep current): ")
            model = input("Enter new model (leave blank to keep current): ")
            color = input("Enter new color (leave blank to keep current): ")
            year = input("Enter new year (leave blank to keep current): ")
            mileage = input("Enter new mileage (leave blank to keep current): ")
            inventory.update_vehicle(index, make or None, model or None, color or None, int(year) if year else None, int(mileage) if mileage else None)
        elif choice == '4': # If the user wants to display the inventory
            inventory.display_inventory()
        elif choice == '5': # If the user wants to save the inventory to a file
            filename = input("Enter filename to save inventory: ")
            inventory.save_inventory_to_file(filename)
        elif choice == '6': # For the user to quit the program gracefully
            break
        else: # Failsafe, if the user does not enter 1 - 6
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()