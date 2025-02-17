import datetime
from CSV_import import *
from Truck import *


# Manually loading the trucks
truck_one = Truck("Truck One",datetime.timedelta(hours=8, minutes=0, seconds=0),[13, 14, 15, 16, 19, 20, 1, 29, 30, 31, 34, 37, 40])
truck_two = Truck("Truck Two",datetime.timedelta(hours=9, minutes=5, seconds=0),[3, 6, 18, 25, 28, 32, 36, 38, 27, 35, 39])
truck_three = Truck("Truck Three",datetime.timedelta(hours=10, minutes=20, seconds=0),[9, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 33])

#function to convert time provided by user into proper format to be processed later
#O(1) Time Complexity
#O(1) Space Complexity
def time_converter(time):

    (hours, minutes, seconds) = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)

    return datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)


#function to return the index of address in address table
#O(1) Time complexity
#O(1) Space Complexity
def address_search(address):
    try:
        return address_details.index(address)
    except:
        return -1


#function to return the distance between two address in distance table
#O(1) Time Complexity
#O(1) Space Complexity
def distance_finder(address1, address2):

    return float(distance_details[address_search(address1)][address_search(address2)])


#nearest neighbor algorithm to find the most efficient delivery route
#O(n) Time complexity
#O(1) Space Complexity
def minimum_distance(truck):
    distances = []

    for items in truck.not_delivered_packages:
        distance = distance_finder(truck.current_address, hash_Table.search(items).address)
        distances.append(distance)

    min_distance = min(distances)
    min_distance_index = distances.index(min_distance)

    return min_distance_index, min_distance


#function handles all delivery tasks, it checks for nearest neighbor and use that as next location to deliver location
#once truck reaches the destination it marks package delivered, add to total miles, and total time it took to take from last to current destination
#O(n^2) time complexity
#O(1) space complexity
def package_deliveries(truck):

    # updates the status of packages to en_route once the truck departs
    for items in truck.not_delivered_packages:
        hash_Table.search(items).status = "En Route"
        hash_Table.search(items).truck_id = truck.truck_id
        hash_Table.search(items).departure_time = truck.departure_time
    truck.current_time = truck.departure_time

    if truck.current_time >= time_converter("10:20:00"):
        hash_Table.search(9).address = "410 S State St"

    #loops and deliver pakages until all the packages are delivered
    while len(truck.not_delivered_packages) > 0:
        min_distance_index, min_distance = minimum_distance(truck)

        #find the nearest neighbor and use that for the next destination
        truck.current_address = hash_Table.search(truck.not_delivered_packages[min_distance_index]).address

        #update milage as packages are delivered at each stop
        truck.distance_travelled += min_distance

        #update time as packages are being delivered
        truck.current_time += datetime.timedelta(hours= min_distance/18)


        #updating status and time of delivery of packages as they are being delivered
        hash_Table.search(truck.not_delivered_packages[min_distance_index]).status = "Delivered"
        hash_Table.search(truck.not_delivered_packages[min_distance_index]).delivery_time = truck.current_time

        #moving packages from not_Delivered to delivered list in the system
        truck.packages_delivered.append(truck.not_delivered_packages[min_distance_index])
        truck.not_delivered_packages.remove(truck.not_delivered_packages[min_distance_index])

    #adding distance and time to hub from last delivery location
    distance_to_hub = distance_finder(hash_Table.search(truck.packages_delivered[len(truck.packages_delivered)-1]), truck.end_address)
    truck.distance_travelled += distance_to_hub
    truck.current_time += datetime.timedelta(hours= distance_to_hub/18)
    truck.end_time = truck.current_time

    #Printing Truck's statues
    print("Truck: " + str(truck.truck_id))
    print("Departed from Hub at: " + str(truck.departure_time))
    print("Arrived at Hub at: " + str(truck.end_time))
    print("Total Distance Travelled: " + str(truck.distance_travelled))
    print("Packages on truck " + str(truck.packages_delivered) +" \n")




