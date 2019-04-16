# Jordan Leung
# 2/14/2019

# 7-10 Dream Vacation
# dictionary type that holds all the responses, with a name (key) and a place (value)
responses = {}

#flag for if polling is active
polling = True

while polling:
    # ask user his/her name
    prompt_name = "Hello there! What is your name? "
    # store the name
    name = input(prompt_name)
    prompt_place = "If there was one place that you could go visit, what place would that be? "
    # store the place
    place = input(prompt_place)
    # store the inputs into the dictionary
    responses[name] = place
    # asks user if they want to continue to poll
    prompt_repeat = "Next Person? "
    prompt = input(prompt_repeat)
    # decides to stop polling if answered no
    while prompt != 'yes':
        if prompt == 'no':
            polling = False
            break
        else:
            prompt = input("Please enter either yes or no: ")

print("\nThese are the results that was entered: ")
for name, place in responses.items():
    print(name +
          " would like to go visit " +
          place)
