# your code goes here
from sys import argv
from random import choice

filename = argv[1]

text = open(filename)

ratings = {}

user_prompt = """
Press A if you want to see all of the restaurant ratings,
B if you would like to add a new restaurant,
C if you would like to quit,
D if you would like to update a random restaurant rating,
E if you would like to choose restaurant to update.

>> """

def print_alphabetically(dictionary_to_unpack):
    """Prints dictionary alphabetically"""

    for restaurant, rate in sorted(dictionary_to_unpack.iteritems()):
        print "{} is rated at {}." .format(restaurant, rate)



for line in text:
    # unpacks line into restaurant name and restaurant rating
    restaurant, rate = line.rstrip().split(':')
    ratings[restaurant] = int(rate)

while True:
    user_input = raw_input(user_prompt).lower()
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
    elif user_input == "d":
        random_restaurant = choice(ratings.keys())
        print random_restaurant, ratings[random_restaurant]
        updated_restaurant_rating = int(raw_input('Updated restaurant rating: '))
        ratings[random_restaurant] = updated_restaurant_rating
        print_alphabetically(ratings)
    elif user_input == "e":
        chosen_restaurant = raw_input("What restaurant would you likt to update? ")
        updated_restaurant_rating = int(raw_input('Updated restaurant rating: '))
        ratings[chosen_restaurant] = updated_restaurant_rating
        print_alphabetically(ratings)
    else:
        print "Please enter a valid input."


    
