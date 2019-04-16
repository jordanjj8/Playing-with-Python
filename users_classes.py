# Jordan Leung
# 2/18/2019

# 9-3 users
number = 0
class User():
    """"represents the user inputted into the system"""
    def __init__(self, first_name, last_name, age, gender):
        """Initalizes the attributes of the user """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """"describes the user """
        description = "User #" + str(number) + " is "
        description += self.first_name.title() + " " + self.last_name.title()
        description += " who is currently " + str(self.age) + " years old and is a " + self.gender
        return(description)

    def increment_login_attempts(self):
        """increments login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """rests the number of login attempts to 0"""
        self.login_attempts = 0

me = User('Jordan', 'Leung', 23, 'male')
friend = User('jack', 'black', 45, 'male')
print(me.describe_user())
number += 1
print(friend.describe_user())

me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
print(me.login_attempts)
