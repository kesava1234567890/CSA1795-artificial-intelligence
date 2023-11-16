import math

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
def nearest_neighbor(start, cities):
    unvisited_cities = set(cities)
    unvisited_cities.remove(start)
    current_city = start
    path = [current_city]
    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: distance(current_city, city))
        path.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city
    path.append(start)
    return path
cities_list = [
    (0, 0),
    (1, 3),
    (2, 8),
    (5, 7),
    (3, 5)
]

start_city = cities_list[0]  # Choosing the first city as the starting city
route = nearest_neighbor(start_city, cities_list)

print("The approximate shortest path for the Traveling Salesman Problem:")
print(route)
