

#Notes: Dictionaries
#dictionaries are the Python implementation of an abstract data type, known in computer science as an associative array
#dictionaries are unordered key-value-pairs
#Like lists they can be easily changed, can be shrunk and grown at run time
#difference between lists and dictionaries? A list is an ordered sequence of objects, whereas dictionaries are unordered sets.
# But the main difference is that items in dictionaries are accessed via keys and not via their position.
#Similar to associative arrays in other programming languages
#Element in dictionary consists of (key,value)
#Indexed by keys and hence keys need to be unique

#Example: 1. Dictionary Creation using {}
city_population = {"New York City":8550405, "Los Angeles":3971883, "Toronto":2731571, "Chicago":2720546, "Houston":2296224, "Montreal":1704694, "Calgary":1239220, "Vancouver":631486, "Boston":667137}
print("--------Print All Values--------------")
#Print all the values
print("Printing all elements of dictionary:",city_population)

#Fetching value from a specific key
print("Population of Toronto is:",city_population['Toronto'])

#Updating the value for population of Tornoto
city_population['Toronto']=34
city_population['toronto']=44
print("Updated Population of Toronto is:",city_population['Toronto'])

#print(city_population["London"]) # keyerror becasue London key not there
city_population["London"]=23432 # new entry for London in dict
print(city_population["London"]) # success
print("Printing all elements of dictionary:",city_population)

#Defining Duplicate Keys
city_population = {"New York City":8550405,"New York City":405,"New York City":805, "Los Angeles":3971883, "Toronto":2731571, "Chicago":2720546, "Houston":2296224, "Montreal":1704694, "Calgary":1239220, "Vancouver":631486, "Boston":667137}
print(city_population) # No error but only one key - for "New York City" is accepted

#Iterating the dictionary
print("---- Iterating the Dictionary ------")
for key in city_population:
    print(key)

for key1 in city_population:
    print(key1,':',city_population[key1])

print("--------Print Individual Key Values : items()-------------")
#items() fetches the key and value pair
for mykey,myvalue in city_population.items():
    print(mykey,':',myvalue)

print("--------Print Individual Key Values and get()-------------")
#Fetching Data: If we want to get the population of one of those cities, all we have to do is to use the name of the city as an index
print(city_population["New York City"])
print(city_population["Boston"])
#Above method would return a key Error in case if the key does not exist

#Another method to access the values via the key consists in using the get() method.
# Does not raise an error if an index doesn't exist
print("Using the get method Key exists:",city_population.get("Boston"))
print("Using the get method key does not exist:",city_population.get("Boston1")) # No keyerror, returns None object

if not city_population.get("Boston1"):
    print("Key does not exists")
else:
    print("Key exists")

del city_population["Boston"]
#Check if the key is existing using "in"
print("London" in city_population)
# If the key is not available print a message
print(city_population.get("Boston1","Country population Unavailable"))
# Key with no value
city_population['newKey']=None
print("Key with no value:",city_population['newKey'])
print(city_population)

#Update method in dictionary - Existing keys are updated with new values and non-exisiting key-value pairs are added
print("Dictionary before updation :",city_population)
New_city_population = {"Newark":800,"New York City":400,"Los Angeles":3000, "Toronto":0}
city_population.update(New_city_population)
print("Updated Dictionary :",city_population)

#Working with multiple dictionaries
en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
print(en_de)
print(en_de["red"])
de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}
print("The French word for red is: " + de_fr[en_de["red"]])
print("All the Keys:",de_fr.keys())
print("All the Values:",de_fr.values())

#Example: Nested Dictionaries
#create a dictionary of dictionaries
dictionaries = {"en_de1" : en_de, "de_fr1" : de_fr }
print("Dictionary of Dictionaries:",dictionaries)
print("Fetch value from Dictionary of Dictionaries:",dictionaries["de_fr1"]["blau"])
print("The French word for red is: " + dictionaries["de_fr1"].get(dictionaries["en_de1"]["red"]))


#pop() is used to take an element out of dict - actually removes item from dict
colors= en_de.pop("red")
print("Remove an element from the stack using POP:",colors)
#if we try to access a key, which is not contained in the dictionary it raises a KeyError. So pop has another argument , which can be used as a default value
colors= en_de.pop("red","Element Does not exist")
print("Default value after removing the element using pop:",colors)

#popitem() is a method of dict, which doesn't take any parameter and removes and returns an arbitrary (key,value) pair as a 2-tuple. If popitem() is applied on an empty dictionary, a KeyError will be raised.
(color,de)=en_de.popitem()
print("Pop Item returning an arbitary value:",(color,de))
(color,de)=en_de.popitem()
print("Pop Item again:",(color,de))
print("Dictionary After Popping Items:",en_de)
