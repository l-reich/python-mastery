import readrides

rows = readrides.read_rides_as_dicts("Data/ctabus.csv")

from collections import Counter

# 1
bus_routes = {row["route"] for row in rows}
number_of_bus_routes = len(bus_routes)
print(number_of_bus_routes)


# 2
pass

# 3
ride_counter = Counter()
for row in rows:
    ride_counter[row["route"]] += row["rides"]

print(ride_counter)


# 4
rows_01 = [row for row in rows if row["date"]]
