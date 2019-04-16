# Jordan Leung
# 2/13/2019

# 5-8 Hello Admin
usernames = ['jjleung', 'nubcake', 'jordanjj8', 'jordanl', 'jjleung88']
#usernames = []

if usernames:
    for username in usernames:
        if username == 'jjleung':
            print("Hello Student, would you like to see your grades?")
        else:
            print("Hello boob, you have entered old usernames that Jordan used to use...")
else:
    print("Please type in usernames! ")


# 5-10 checking new usernames
current_users = usernames[:]
new_users = ['hello', 'singer_babe', 'jordanl', 'guitar_lover', 'jjleung']

for user in new_users:
    if user in current_users:
        print("Please replace " + user + " and add a new username")
    else:
        print("Adding username " + user + " to the list")


