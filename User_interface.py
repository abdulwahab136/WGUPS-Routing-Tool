from Package_Delivery import *

#This function provides the user interface that customer utilizes to see all the information required
#O(n) Time complexity
#O(1) Space Complexity
def user_interface():

    #print the total distance travelled by all trucks
    total_distance = truck_one.distance_travelled+truck_two.distance_travelled+truck_three.distance_travelled
    print("Total Distance travelled by all trucks: {:.2f} \n\n".format(total_distance))

    not_quit = True
    #print("Select an option from the following menu")
    while not_quit:
        print("[1] package detail at specific time")
        print("[2] information about all packages at specific time")
        print("[0] quit")

        user_input = int(input("Enter your choice: "))



        if user_input == 1:

            try:
                time = input("Enter time in HH:MM:SS format: ")
                converted_time = time_converter(time)
                package_lookup_id = int(input("Enter package id: "))
                package = hash_Table.search(package_lookup_id)
                print(package.package_details(converted_time))
            except:
                print("Invalid input")

        elif user_input == 2:

            try:
                time = input("Enter time in HH:MM:SS format: ")
                converted_time = time_converter(time)
                for values in range(1, 41):
                    package = hash_Table.search(values)
                    print(package.package_details(converted_time))

            except:
                print("Invalid input")

        elif user_input == 0:
            print("Be Safe, Have a nice day!")
            not_quit = False

        else:
         print("Invalid input")