# Jordan Leung
# 3/28/2019
#exlist = [1, 'hello', 2]
#print(exlist)
#print(exlist[1])
#x = 1 + exlist[2]
#print(x)
# 9-13 OrderedDict Rewrite:

from collections import OrderedDict


#glossary = {}
glossary = OrderedDict()

glossary['dictionary'] = 'type of data that allows you to connect pieces of related information, ' \
                          'essentially creating key-value pairs'
glossary['list'] = 'a collection of items in a particular order, in a way, ' \
                    'it is a vector of whatever types you\'d like'

glossary['tuple'] = 'Essentially an immutable list, using parentheses to create the type'

#print out key and value from the glossary dictionary.
for word, definition in glossary.items():
    print(word.title() + ': ' + definition + ".")

# 9-14 Dice Exercise
from random import randint
x = randint(1,6)
print(x)
