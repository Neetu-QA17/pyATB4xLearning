# ORDERED DICTIONARY - it remembers the insertion order
from collections import OrderedDict

d = {"address": "UP", "name": "Neetu", "Age": 29, "ID": 627874}  # Normal Dictionary
print(d)

od = OrderedDict()
od['Banana'] = 2
od['Apple'] = 1
od['Orange'] = 1
od['Grapes'] = 10
print(od)
