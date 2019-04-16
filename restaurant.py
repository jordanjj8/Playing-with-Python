# Jordan Leung
# 2/18/2019

# restaurants 9-1

class Restaurant():
    """A class to represent a restaurant in the simplest ways"""

    def __init__(self, restaurant_name, cuisine_type):
        """"Initializes attributes to describe the restaurant"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """prints out the name and type of restaurant it is"""
        # checks to see if the article needs to be a or an
        if (self.type[0] == 'a') or (self.type[0] == 'e') or (self.type[0] == 'i') or (self.type[0] == 'o') or (self.type[0] == 'u'):
            article = 'an '
        else:
            article = 'a '
        description = self.name.title() + " is " + article + self.type.title() + " type of restaurant."

        return description

    def open_restaurant(self):
        """"prints out a message indicating that the restaurant is open"""
        message = self.name.title() + " is currently open!"
        return message

    def set_number_served(self, number):
        """sets the attribute to a number specified """
        self.number_served = number

    def increment_number_served(self, day_served):
        """increments the attribute by a number specified"""
        self.number_served += day_served

class IceCreamStand(Restaurant):
    """"represents aspects of an dessert restaurant, specifically an ice cream stand"""

    def __init__(self, restaurant_name, flavors, cuisine_type='dessert'):
        "Initializes attributes of the parents and then attributes specific to the ice cream stand"
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """"Displays the flavors that the ice cream stand has"""
        i = 0
        # variable that holds the string that needs to be displayed
        display = "Flavors include: "
        for flavor in self.flavors:
            display += "\n\t" + self.flavors[i].title()
            i += 1
        return(display)

# what is run by main
my_restaurant = Restaurant('all you can eat clams', 'asian')
print(my_restaurant.describe_restaurant())
print(my_restaurant.open_restaurant())

your_restaurant = Restaurant('all you can eat noodles', 'italian')
print(your_restaurant.describe_restaurant())
print(your_restaurant.open_restaurant())

# exercises pertaining to the ice cream stand
j_list = ['green tea', 'chocolate', 'vanilla', 'taro']
jj_ice = IceCreamStand("Jordan's Ice", j_list, cuisine_type="asian dessert")
#jj_ice = IceCreamStand("Jordan's Ice", j_list)
print(jj_ice.display_flavors())
print(jj_ice.describe_restaurant())

