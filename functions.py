# Jordan Leung
# 2/14/2019

# 8-5 cities

def describe_city(city_name, country = 'China'):
    """Describes where in what oountry the city is in"""
    result = '\n' + city_name + ' is in ' + country
    return result


one = describe_city('shanghai')
two = describe_city('beijing', 'China')
three = describe_city(country = 'Britain', city_name = 'hong kong')

print(one)

# magicians
magicians = []
#flag for polling
polling = True

while polling:
    # asks for input
    magician = input("Tell me the name of a great magician: ")
    magicians.append(magician)
    repeat = input("Type 1 if you have another name. If not, Type 2: ")
    # enters into a while to ensure that either 1 or 2 is typed in
    while repeat != '1':
        if repeat == '2':
            polling = False
            break
        else:
            repeat = input("Type either 1 or 2: ")
    # value is only converted to integer after it is verified that either 1 or 2 was typed in
    repeat = int(repeat)

def make_great(list):
    for num in range(0, len(list)):
        list[num] = "The Great " + list[num]

def show_magicians(people):
    """Prints out the names of all the people in the list"""
    for person in people:
        print(' ' + person.title() + ' ')

print("Here are the names of the magicians: ")
show_magicians(magicians)

print("The Great Ones are: ")
copy = magicians[:]
make_great(copy)
show_magicians(copy)
print("Original: ")
show_magicians(magicians)

