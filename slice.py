# Jordan Leung
# 2/13/2019

# printing out what is given
print("Given: ")
cubes = [num**3 for num in range(1,11)]
print(cubes)

# printing out the first three items
print("The first three items in the list are: ")
print(cubes[:3])

# printing out the middle of the list
print("Three items from the middle of the list are: ")
mid = int(len(cubes)/2)
mid_Start = int(mid - 1)
mid_End = int(mid + 2)
print(cubes[mid_Start:mid_End])

# printing out the last three items in the list
print("The last three iems in the list are: ")
print(cubes[-3:])

# making a copy of a list by slicing and verifying that they are stored seperately 
my_fav_foods = ['cookies', 'clams', 'pickles']
friends_foods = my_fav_foods[:]

my_fav_foods.append('okura')
friends_foods.append('buns')
print("My favorite foods include: ")
for food in my_fav_foods:
    print(food)
print("My friend's favorite foods include: ")
for food in friends_foods:
    print(food)

