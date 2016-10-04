# your code goes here
from sys import argv

filename = argv[1]

text = open(filename)

ratings = {}

def print_alphabetically(dictionary_to_unpack):
    """Prints dictionary alphabetically"""

    for restaurant, rate in sorted(dictionary_to_unpack.iteritems()):
        print "{} is rated at {}." .format(restaurant, rate)



for line in text:
    # unpacks line into restaurant name and restaurant rating
    restaurant, rate = line.rstrip().split(':')
    ratings[restaurant] = int(rate)

while True:
    user_input = raw_input("\nPress A if you want to see all of the restaurant ratings,\n"
                           "B if you would like to add a new restaurant, \n"
                           "or C if you would like to quit.\n >> ").lower()
    if user_input == "a":
        print_alphabetically(ratings)
    elif user_input == "b":
        user_restaurant = raw_input("What restaurant would you like to add? ")
        user_rating = int(raw_input("What rating would you give that restaurant? "))
        ratings[user_restaurant] = user_rating
        print_alphabetically(ratings)
    elif user_input == "c":
        print "You are now exiting the Rating Application. Good Bye!"
        break
    else:
        print "Please enter a valid input."


    
