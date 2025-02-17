# Package Class
class Package:
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, special_notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.departure_time = None
        self.delivery_time = None
        self.status = "at_hub"
        self.truck_id = None

    #Function returns the details of a single package, returns details as id, address, city, zipcode, deadline, weight, notes and status
    #O(1) Time complexity
    #O(1) Space Complexity
    def package_details(self, current_time):
        from Package_Delivery import time_converter

        if self.package_id == 9 and current_time >= time_converter("10:20:00"):
            self.address = "410 S State St"

        elif self.package_id == 9 and current_time <= time_converter("10:20:00"):
            self.address = "300 State St"

        if current_time >= self.delivery_time:
            time = self.delivery_time
            self.status = "Delivered \t Delivery time: " + str(time)

        elif self.delivery_time > current_time > self.departure_time:
            self.status = "En Route"

        else:
            self.status = "at Hub"
        delivery_address = f"{self.address}, {self.city}, {self.state}, {self.zipcode}"
        return f"Package ID: {self.package_id:<2} \t Delivery_Address: {delivery_address:<65} \t Delivery Deadline: {self.deadline:<10} \t Delivery Status: {self.status:<65} \t Assigned Truck: {self.truck_id}"


