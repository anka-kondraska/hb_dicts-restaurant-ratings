# your code goes here
from sys import argv

filename = argv[1]

text = open(filename)

ratings = {}
for line in text:
    restaurant, rate = line.rstrip().split(':')
    ratings[restaurant] = int(rate)

for restaurant, rate in sorted(ratings.iteritems()):
    print "{} is rated at {}." .format(restaurant, rate)

user_restaurant = raw_input("What restaurant would you like to add? ")
user_rating = int(raw_input("What rating would you give that restaurant? "))

ratings[user_restaurant] = user_rating

for restaurant, rate in sorted(ratings.iteritems()):
    print "{} is rated at {}." .format(restaurant, rate)


    
