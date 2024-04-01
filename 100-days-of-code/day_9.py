# Python dictionaries
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have key/value pairs.

# Create a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieve item value from dictionary by its key
print(programming_dictionary["Bug"])
# will return item: 'An error in a program that prevents the program from running as expected.'

# Add new items to dictionary - appends to end
programming_dictionary["Loop"] = "The action of doing something over and over again"

print(f"\n{programming_dictionary}")

# Create an empty dictionary
empty_dictionary = {}
empty_dictionary["key"] = "value"
print(f"\n{empty_dictionary}\n")

# Wipe an existing dictionary
empty_dictionary = {} # note, the same as creating an empty dictionary
print(empty_dictionary)

programming_dictionary["While loop"] = "A loop that continues"
print(f"\n{programming_dictionary}")

# Edit, or update an item in a dictionary
programming_dictionary.update({"While loop": "A loop that continues to run until a condition is met"})
print(f"\n{programming_dictionary}")

# Loop through a dictionary and print all keys or value
for key in programming_dictionary:
    print(key) # prints all keys
    print(programming_dictionary[key]) # prints all values

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested list in dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nested dictionaries inside dictionaries
fred_travel_log = {
    "France": {
        "cities_visited": {
            "Paris": {
                "Museums visited": {
                    "Musée du Louvre",
                    "Musée d'Orsay",
                    "Musée Marmottan Monet",
                },
            },
            "Lille" : {
                "Museums visited": {
                    "Palais des Beaux-Arts",
                    "Musée d’Histoire Naturelle"
                },
            },
            "Dijon": {
                "Museums visited": {
                    "Musée des Beaux-Arts",
                },
            },
        },
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": {
            "Berlin": {
                "Museums visited": {
                    "Pergamon Museum",
                    "Gemaldegalerie",
                },
            },
            "Hamburg" : {
                "Museums visited": {
                    "Museum für Kunst und Gewerbe",
                },
            },
            "Stuttgart": {
                "Museums visited": {
                    "Staatsgalerie",
                },
            },
        },
        "total_visits": 6
    },
}

for country in fred_travel_log:
    print(f"\nCountry: {country}")
    for city in fred_travel_log[country]["cities_visited"]:
        print(f"City: {city}")
        for museum in fred_travel_log[country]["cities_visited"][city]["Museums visited"]:
            print(f"Museum: {museum}")
    print(f"Total visits: {fred_travel_log[country]['total_visits']}")


# add a country to a travel log challenge
# following slightly changed for local testing
country = input("\nPlease enter a country: ") # Add country name
visits = int(input("How many times have you visited? ")) # Number of visits
list_of_cities = eval(input("Which cities did you visit? Please enter as a comma seperated list, i.e. 'Paris', 'Lille', etc: ")) # create list from formatted string

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
# Do NOT change the code above 👆

def add_new_country(name, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
