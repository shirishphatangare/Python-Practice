#List
#-List : ordered and mutable. Allows duplicate members.Indexed

countries=["UK","Russia","USA","Japan","Canada"]
print(countries)
hetroList=[1,"one",2,"two",3,"Three",4]
print(type(hetroList))

#Check out the list operations
dir(list)
#Check out the length of list
print("Length of List:",len(hetroList))

#Extracting elements from a list
print("First Element from Countries:",countries[0])
print("Last Element from Countries:",countries[-1])
print("Slicing elements:",countries[2:5])
#Appending to the list: append single element to the list
countries.append("Japan")
#Appending another list to the existing list : extend()
European_countries=["Ireland","Germany","France"]
countries.extend(European_countries)
print ("After appending European Countries:",countries)
#Appending multiple values to the list
countries[len(countries):]=["Burma","Srilanka"]
print ("After appending Multiple Countries:",countries)
#Add a new element at a specific position within the list
countries[5]="Armenia" #If you use indexes to insert an element, if the element exists, it is replaced
print ("Inserting new Countries at specific index position:",countries)
countries.insert(5,"Argentina") #A new element is being pushed to the specfic position. All the existing elements are pushed down

print ("Inserting new Countries by negative index:",countries)
countries[-1] = "Ghana"
print ("Inserting new Countries insert method:",countries)

cities=['Paris','New York','Mumbai']
countries.insert(7,cities)
print("Cities inserted:",countries)
#You could insert into negative indices
cities1=['Pune','London','Bangalore']
countries.insert(-1,cities1)
print("Cities inserted at negative index:",countries)
print(countries[-1])
#Extracting City "New York" from countries
print("Extracting element from a sublist:",countries[7][1])

#Remove elements from the list
#del: Delete values from list basis to inde x position
del countries[7]
del countries[-2]
print("After deleting at index position 7 and -2",countries)
#Delete first 2 elements from the list
del countries[:2]
print("After deleting at first 2 values",countries)
print("Index position 1:", countries[0:2])
#remove : Remove a specific value from the list.
# If there are multiple occourances, it removes the first occourance
countries.remove("France")
print("After removing France from the list:",countries)
# If there is no element to be removed, it raises an error
#List Membership : in and not in
if "France" in countries:
    countries.remove("France")
#Repeatedly Remove all elements of "france" from the list
while ("France" in countries):
    countries.remove("France")

#Arithmetic Operations in List
# + : COncatenation
odd = [1,3,5]+[101,103]
print ("Odd Numbers Concated using +",odd)
# * : Repetition
odd = 3*odd
print("List created with repeated elements:",odd)
#Fetch the Minimum and Maximum Value from a list
print("MinimumValues from Odd:",min(odd))
print("MaximumValues from Odd:",max(odd))
print("Count of Value (103)in Odd:", odd.count(103))
#Find the index of a specific element
print("Index of element 3 in list:",odd.index(3))

#Sorting a List
#sort: Built-in python
odd.sort()
print("Sorted elements of Odd:",odd)
#Sorting countries
print("Index of Burma before Sorting:",countries.index("Burma"))
countries.sort()
print("Sorted Countries:",countries)
print("Index of Burma after Sorting:",countries.index("Burma"))
#Sorting a list of lists
#Sublist is sorted by ascending order of 1st element and then ascending order of second element
numList=[[1,"one"],[20,"Twenty"],[2,"two"],[0,"Zero"]]
numList.sort()
print("Sorting a list of Lists:",numList)
numList.sort(reverse=True)
print("Sorting a list of Lists in Reverse:",numList)


#Custom Sorting
#1. Write a function to define the sort order
def compare_countries_length(country):
    return len(country)
#2. Sorting Countries basis the length
countries.sort(key=compare_countries_length)
print("Sorted on Length:",countries)
#3. Sorting Countries basis the length in reverse order
countries.sort(key=compare_countries_length,reverse=True)
print("Sorted on Length(reverse):",countries)
#Note: Custom sorting may have some performance issues as it may be slower than in-built sort operation
