
#🚨 Do NOT change the code above
#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visitis , list):
    new_city={}
    new_city["country"]=country
    new_city["visits"]=visitis
    new_city["cities"]=list
    travel_log = [
    {
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
    },
    {
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
    ]
    travel_log.append(new_city)
    print(travel_log)










#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
