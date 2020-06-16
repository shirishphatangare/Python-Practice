#Example: Load JSON string into an OrderedDict
# OrderedDict preserves the order in which the keys are inserted. A regular dict doesn’t track the insertion order, and iterating it gives the values in an arbitrary order

import json
from collections import OrderedDict

# OrderedDict
print("Ordering keys")
OrderedData = json.loads('{"John":11, "Emma": 2, "Ault": 3, "Brian": 4}', object_pairs_hook=OrderedDict)
print("Type: ", type((OrderedData)))
print(OrderedData)

# regular Dict
print("Regular Dict")
regularDict = json.loads('{"John":11, "Emma": 2, "Ault": 3, "Brian": 4}')
print("Type: ", type((regularDict)))
print(regularDict)