import json


file = open("2024-02-10 11-50-19.json")
data = json.load(file)


flight_array = []


data_list = data['exchange']['message']['flight_logging']['flight_logging_items']


for row in data_list:
    flight_array.append(row)



print("Oluşturulan flight_array listesi:")
for row in flight_array:
    print (row)
    print("bir satır bitii")
