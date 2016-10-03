# your code goes here
from sys import argv

filename = argv[1]

text = open(filename)

ratings = {}
for line in text:
    ratings_list = line.rstrip().split(':')
    ratings[ratings_list[0]] = ratings.get(ratings_list[0],int(ratings_list[1]))

for restaurant, rate in sorted(ratings.iteritems()):
    print "{} is rated at {}." .format(restaurant, rate)

