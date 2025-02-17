import csv

from Packages import *
from HashTable import *

#initializing distance_details, address_details, hash_Table to store data read from the csv files
distance_details = []
address_details = []
hash_Table = HashTable()

#function reads the package csv file and save the values in hash table, it uses package_id as key and package object to store the attributes
#O(n) Time Complexity
#O(n) Space Complexity
def package_import(filename):


    with open(filename) as file:

        contents = csv.reader(file, delimiter=',')
        for row in contents:

            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zipcode = int(row[4])
            deadline = row[5]
            weight = int(row[6])
            special_notes = row[7]

            hash_Table.insert(package_id, Package(package_id, address, city, state, zipcode, deadline, weight, special_notes))




#funciton reads the address csv file and store values in address_details list
#O(n) Time complexity
#O(n) Space Complexity
def address_import(filename):
    with open(filename) as file:
        contents = csv.reader(file, delimiter=',')

        for row in contents:
            address_details.append(row[2])



#Function reads the distance csv file provided and store values in 2 dimensional list/array
#O(n^2) Space Complexity
#O(n^2) Time Complexity
def distance_import(filename):
    with open(filename) as file:
        contents = csv.reader(file, delimiter=',')

        for row in contents:
            distance_details.append(row)

        for i in range(len(distance_details)):
            for j in range(len(distance_details)):
                distance_details[i][j] = distance_details[j][i]

