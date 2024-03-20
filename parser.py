import json

file = open("2024-02-10 11-50-19.json")
data = json.load(file)

flight_array = []

data_list = data['exchange']['message']['flight_logging']['flight_logging_items']
data_headers = data['exchange']['message']['flight_logging']['flight_logging_keys']

for row in data_list:
    flight_array.append(row)

general_lon = 0.0
general_lat = 0.0

for row in flight_array:
    first_three_elements = row[1:3] 
    general_lon += row[1]
    general_lat += row[2]
    print(first_three_elements)
    print("bir satır bitti")

general_lon = general_lon/len(flight_array)
general_lat = general_lat/len(flight_array)

print("Genel Boylam :")
print(general_lon)
print("Genel Enlem :")
print(general_lat)