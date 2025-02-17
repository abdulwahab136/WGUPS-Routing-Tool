
# Truck Class
class Truck:
    def __init__(self, truck_id, departure_time, packages):
        self.truck_id = truck_id
        self.departure_time = departure_time
        self.not_delivered_packages = packages
        self.truck_capacity = 16
        self.truck_speed = 18
        self.start_address ="4001 South 700 East"
        self.end_address ="4001 South 700 West"
        self.current_address = self.start_address
        self.distance_travelled = float('0.0')
        self.packages_delivered = []
        self.current_time = None
        self.end_time = None

