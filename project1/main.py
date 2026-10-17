###---- Vehicle Service Management System ----###

import random
import string


# ---------- Customer Class ----------

class Customer:
    def __init__(self, customer_name, phone_no, address):
        self.customer_name = customer_name
        self.customer_id = "".join(
            random.choices(string.ascii_letters + string.digits, k=5)
        )
        self.phone_no = phone_no
        self.address = address

    def display(self):
        print("\n----- Customer Details -----")
        print("Customer Name:", self.customer_name)
        print("Customer ID:", self.customer_id)
        print("Phone Number:", self.phone_no)
        print("Address:", self.address)


# ---------- Vehicle Class ----------

class Vehicle:
    def __init__(self, vehicle_no, model, vehicle_type,
                 service_type, customer_id):
        self.vehicle_no = vehicle_no
        self.model = model
        self.vehicle_type = vehicle_type
        self.service_type = service_type
        self.customer_id = customer_id
        self.status = "Pending"

    def display(self):
        print("\n----- Vehicle Details -----")
        print("Vehicle Number:", self.vehicle_no)
        print("Model:", self.model)
        print("Vehicle Type:", self.vehicle_type)
        print("Service Type:", self.service_type)
        print("Customer ID:", self.customer_id)
        print("Service Status:", self.status)


# ---------- Service Center Class ----------

class Service_Center:
    services = {
        "Bike": {
            "General Service": 800,
            "Oil Change": 500,
            "Water Wash": 200
        },
        "Car": {
            "General Service": 1500,
            "Oil Change": 1000,
            "Water Wash": 500
        },
        "Truck": {
            "General Service": 3000,
            "Oil Change": 2000,
            "Water Wash": 1000
        }
    }

    def __init__(self):
        self.customers = []
        self.vehicles = []

    # ---------- Register Customer ----------

    def register_customer(self):
        name = input("Enter customer name: ").strip()
        phone_no = input("Enter phone number: ").strip()
        address = input("Enter address: ").strip()

        if not name or not phone_no or not address:
            print("All customer details are required!")
            return

        customer = Customer(name, phone_no, address)

        # Check whether customer ID already exists
        while any(c.customer_id == customer.customer_id
                  for c in self.customers):
            customer.customer_id = "".join(
                random.choices(string.ascii_letters + string.digits, k=5)
            )

        self.customers.append(customer)

        print("\nCustomer registered successfully!")
        print("Customer ID:", customer.customer_id)

    # ---------- Add Vehicle ----------

    def add_vehicle(self):
        customer_id = input("Enter customer ID: ").strip()

        customer = None

        for c in self.customers:
            if c.customer_id == customer_id:
                customer = c
                break

        if customer is None:
            print("Customer not found! Please register first.")
            return

        vehicle_no = input("Enter vehicle number: ").strip().upper()

        if not vehicle_no:
            print("Vehicle number cannot be empty!")
            return

        # Prevent duplicate vehicle numbers
        for v in self.vehicles:
            if v.vehicle_no == vehicle_no:
                print("This vehicle is already registered!")
                return

        model = input("Enter vehicle model: ").strip()
        vehicle_type = input(
            "Enter vehicle type (Bike/Car/Truck): "
        ).strip().capitalize()

        if vehicle_type not in self.services:
            print("Invalid vehicle type! Choose Bike, Car, or Truck.")
            return

        if not model:
            print("Vehicle model cannot be empty!")
            return

        vehicle = Vehicle(
            vehicle_no,
            model,
            vehicle_type,
            "Not Selected",
            customer.customer_id
        )

        self.vehicles.append(vehicle)
        print("Vehicle added successfully!")

    # ---------- View Customers ----------

    def view_customer(self):
        print("\n1. Search Customer by ID")
        print("2. Display All Customers")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            customer_id = input("Enter customer ID: ").strip()

            for c in self.customers:
                if c.customer_id == customer_id:
                    c.display()
                    return

            print("Customer not found!")

        elif choice == "2":
            if not self.customers:
                print("No customers registered!")
                return

            for c in self.customers:
                c.display()
                print("-" * 30)

        else:
            print("Invalid choice!")

    # ---------- View Vehicles ----------

    def view_vehicles(self):
        print("\n1. Search Vehicles by Customer ID")
        print("2. Display All Vehicles")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            customer_id = input("Enter customer ID: ").strip()
            found = False

            for v in self.vehicles:
                if v.customer_id == customer_id:
                    v.display()
                    found = True

            if not found:
                print("No vehicles found for this customer!")

        elif choice == "2":
            if not self.vehicles:
                print("No vehicles registered!")
                return

            for v in self.vehicles:
                v.display()
                print("-" * 30)

        else:
            print("Invalid choice!")

    # ---------- View Services / Select Service ----------

    def view_services(self):
        vehicle_no = input("Enter vehicle number: ").strip().upper()

        for v in self.vehicles:
            if v.vehicle_no == vehicle_no:
                service_list = list(
                    self.services[v.vehicle_type].items()
                )

                print("\nAvailable Services")

                for i, (service, price) in enumerate(service_list, 1):
                    print(f"{i}. {service} - ₹{price}")

                choice = input("Select service number: ").strip()

                if not choice.isdigit():
                    print("Please enter a valid number!")
                    return

                choice = int(choice)

                if 1 <= choice <= len(service_list):
                    service_name, price = service_list[choice - 1]
                    v.service_type = service_name

                    print("Service selected:", service_name)
                    print("Service price: ₹", price)
                else:
                    print("Invalid service choice!")

                return

        print("Vehicle not found!")

    # ---------- Generate Bill ----------

    def generate_bill(self):
        vehicle_no = input("Enter vehicle number: ").strip().upper()

        for v in self.vehicles:
            if v.vehicle_no == vehicle_no:

                if v.service_type == "Not Selected":
                    print("Please select a service first!")
                    return

                price = self.services[v.vehicle_type][v.service_type]

                print("\n========== SERVICE BILL ==========")
                print("Customer ID:", v.customer_id)
                print("Vehicle Number:", v.vehicle_no)
                print("Vehicle Model:", v.model)
                print("Vehicle Type:", v.vehicle_type)
                print("Service:", v.service_type)
                print("Service Status:", v.status)
                print("Total Amount: ₹", price)
                print("==================================")
                return

        print("Vehicle not found!")

    # ---------- Main Menu ----------

    def main_menu(self):
        while True:
            print("\n===== Vehicle Service Management System =====")
            print("1. Register Customer")
            print("2. Add Vehicle")
            print("3. View Customers")
            print("4. View Vehicles")
            print("5. View Services / Select Service")
            print("6. Generate Bill")
            print("7. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.register_customer()

            elif choice == "2":
                self.add_vehicle()

            elif choice == "3":
                self.view_customer()

            elif choice == "4":
                self.view_vehicles()

            elif choice == "5":
                self.view_services()

            elif choice == "6":
                self.generate_bill()

            elif choice == "7":
                print("Thank you for using our service center!")
                break

            else:
                print("Invalid choice! Please try again.")


# ---------- Run the Project ----------

center = Service_Center()
center.main_menu()          