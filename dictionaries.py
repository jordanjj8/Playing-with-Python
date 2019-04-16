# Jordan Leung
# 2/14/2019

# Rivers 6-5
major_rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'huang he': 'china',
    }

# printing the river and the country
for river, country in major_rivers.items():
    print('The ' +
          river.title() +
          ' River runs through the ' +
          country.title())

# 6-9 favorite places
favorite_places = {
    'don': ['korea','davis'],
    'preston': ['japan', 'china', 'los angeles'],
    'bryan':['cmu', 'kg','china'],
    }
for name, places in favorite_places.items():
    print("\n" + name.title() + '\'s favorite places include:')
    for place in places:
        print("\t" + place.title())
print("Here are the places mentioned: ")
for places in favorite_places.values():
    print(places)

    