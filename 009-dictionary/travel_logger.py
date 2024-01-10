travel_log = [
    {
        "country": "France",
        "cities": ["Paris", "Lille", "Dijon"],
        "visits": 12
    },
    {
        "country": "Germany",
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
        "visits": 5
    }
]

def add_new_country(country: str, visits: int, cities: list[str]) -> None:
    travel_log.append({
        "country": country,
        "cities": cities,
        "visits": visits
    })


country = input("Enter a country : ")
visits = int(input("Enter the number of visits to that country : "))
list_of_cities = eval(input("Enter a python list of cities visited in that country : "))

add_new_country(country, visits, list_of_cities)

for entry in travel_log:
    print(f"I've been to {entry["country"]} {entry["visits"]} time(s). My favorite city is {entry["cities"][0]}")
