#Sets
#- Unordered: Does not maintain the sequence of the data that is being added
#- No Duplicates
#- Mutable

#Creating a set
contactemails={"allen@gmail.com","tony@gmail.com","sam@yahoo.com","sherry@yahoo.com","tony@gmail.com"}
print("Type of email datastructure:",type(contactemails))
print("Contact Emails:",contactemails)

#Duplicates are not added to the set
contactemails.add("tony@gmail.com")
print("Contact Emails - Element addded:",contactemails)

contactemails.add("Samuel@yahoo.com")
print("Contact Emails - Element addded:",contactemails)
#Remove elements from the set
contactemails.remove("Samuel@yahoo.com")
print("Contact Emails - Element addded:",contactemails)

#Check if the element exists before adding
if "allen@gmail.com" in contactemails:
    contactemails.remove("allen@gmail.com")
else:
    contactemails.add("allen1@gmail.com")
print("Contact Emails - Conditional Inclusion:",contactemails)


#Create a set from a list: set()
countriesset=set(["UK","Russia","USA","Japan","Canada"])
print("Set of countries:",countriesset)

#Set Operations
#Union Operation(|)
EuropeanCountriesSet=set(["Ireland","Germany","France"])
allcountries=countriesset|EuropeanCountriesSet
print("union of Sets:",allcountries)
#Intersect Operation(&)
countriesIntersect=allcountries & {"UK","Ireland","Australia","Africa"}
print("Insertsection of sets:",countriesIntersect)
#Symmetric Differences (^)
diffcountries=allcountries ^ {"UK","Ireland","Australia","Africa"}
print("Differences between the sets:",diffcountries)

#FronzenSets: Immutable and hashable
fcountriesset=frozenset(["UK","Russia","USA","Japan","Canada"])
print("Frozen Set of countries:",fcountriesset)
#fcountriesset.add("Berlin") # 'frozenset' object has no attribute 'add'
print("Frozen Set of countries:",fcountriesset)

#Convert a tuple to set
emails=("x@gmail.com","y@yahoo.com","z@hotmail.com")
print("tuple to set: ", set(emails))
