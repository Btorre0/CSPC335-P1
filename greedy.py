# Hamiltonian Problem || Greedy Approach Implementation
# Author: Beatriz Torres Archundia
# CSUF Email: Btorre0@csu.fullerton.edu

def city_starting(distances, fuel, mpg): 
    total_fuel = 0
    current_fuel = 0 
    start_city = 0

    n = len(distances)

    for i in range(n):
        fuel_available = fuel[i] * mpg
        fuel_required = distances[i]
        net_fuel = fuel_available - fuel_required

        total_fuel += net_fuel
        current_fuel += net_fuel

        if current_fuel < 0:
            start_city = i + 1
            current_fuel = 0
    
    if total_fuel >= 0:
        return start_city
    return -1

# test cases

# test 1:
city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

print("test 1:", city_starting(city_distances, fuel, mpg))

# test 2:

city_distances = [10, 2, 31, 5, 7]
fuel = [2, 2, 3, 3, 9]
mpg = 20

print("test 2:", city_starting(city_distances, fuel, mpg))

# test 3:

city_distances = [3, 5, 7, 10, 12]
fuel = [3, 2, 1, 0, 5]
mpg = 15

print("test 3:", city_starting(city_distances, fuel, mpg))

# test 4:

city_distances = [7, 10, 15, 20, 25]
fuel = [1, 2, 3, 4, 5]
mpg = 5

print("test 4:", city_starting(city_distances, fuel, mpg))