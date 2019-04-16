# Jordan Leung
# 2/11/2019

guests = ['Henry', 'Sifu Jeff', 'Tayler', 'Mat']
print(guests)
print(guests[0] + ", " + guests[1] + ", " + guests[2] + ", and " + guests[3] + " are invited to this family dinner!")
print("But I just realized that not everyone on the list are part of my family...")

print(guests[0] + " and " + guests[1] + 'need to be replaced')

# modifying family names
guests[0] = "Dad"
guests[1] = "Mom"
print(guests)

# add family members
print("Now adding other family members...")
guests.insert(2,'Preston')
guests.insert(3,'Kaden')
print(guests)

# Just immediate family
print("Now the boss wants just the immediate family...sorry cuz")
guests.remove("Mat")
guests.remove("Tayler")
print(guests)