#Name: Abdul Wahab
#Student ID: 011510437
from User_interface import *


#Main class, imports from while, call the package_Delivery function and starts user interface for the customer
class Main:
    print("Western Governors University Parcel Service Program")


    #importing csv import functions to read data from CSVs to process and store in respective data variables
    package_import("Packages_Info.csv")
    address_import("Address_Info.csv")
    distance_import("Distance_Info.csv")


    #Calling package_deliveries function for each truck
    package_deliveries(truck_one)
    package_deliveries(truck_two)
    package_deliveries(truck_three)

    #Calling User_interface
    user_interface()






