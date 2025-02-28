def starting_city(distances, fuel, mpg):
    total_fuel = 0
    current_fuel = 0 
    start_city = 0

    n = len(distances)

    if n == 0:
        return -1
    if len(fuel) != n:
        return
    

    for i in range(n):
        # checking if actual distance that can be cover if greater than city
        available_fuel = fuel[i] * mpg
        fuel_balance = available_fuel - distances[i]
        
        total_fuel += fuel_balance
        current_fuel += fuel_balance
       
        if current_fuel < 0:
            start_city = i + 1
            current_fuel = 0
    if total_fuel >= 0:
        return start_city
    else:
        return -1


# test cases

# test 1:
city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

print("test 1:")
print("city_distances", city_distances)
print("fuel", fuel)
print("mpg", mpg)
print("The preferred starting city for the sample above is city ",  starting_city(city_distances, fuel, mpg))
print()

# test 2:

city_distances = [10, 35, 24, 10, 15]
fuel = [1, 2, 3, 3, 2]
mpg = 10

print("test 2:")
print("city_distances", city_distances)
print("fuel", fuel)
print("mpg", mpg)
print("The preferred starting city for the sample above is city ", starting_city(city_distances, fuel, mpg))
print()

# test 3:

city_distances = [15, 20, 25, 30, 35]
fuel = [4, 3, 2, 3, 4]
mpg = 10

print("test 3:")
print("city_distances", city_distances)
print("fuel", fuel)
print("mpg", mpg)
print("The preferred starting city for the sample above is city ", starting_city(city_distances, fuel, mpg))
print()

# test 4:

city_distances = [7, 10, 15, 20, 25]
fuel = [4, 2, 3, 4, 5]
mpg = 3

print("test 4:")
print("city_distances", city_distances)
print("fuel", fuel)
print("mpg", mpg)
print("The preferred starting city for the sample above is city ", starting_city(city_distances, fuel, mpg))