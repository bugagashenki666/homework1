from random import random
print("Расстояние между точками A и B:")
distance = int(input())
print("Бака хватает на расстояние: ")
gas_tank_distance = int(input())
print("Количество заправок между точками A и B")
count_of_gas_stations = int(input())
distances_between_gas_stations = [0]

for i in range(count_of_gas_stations):
    distances_between_gas_stations.append(int(random() * distance))
distances_between_gas_stations.sort()
print(distances_between_gas_stations)

left_border_of_range = 0
right_border_of_range = 0
i = 0
while i in range(len(distances_between_gas_stations)):
    if distances_between_gas_stations[i] - left_border_of_range > gas_tank_distance:
        right_border_of_range = distances_between_gas_stations[i - 1]
        break
    i += 1
print("диапазон: %i - %i" % (left_border_of_range, right_border_of_range))