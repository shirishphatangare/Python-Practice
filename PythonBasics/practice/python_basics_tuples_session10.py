#Tuples:
#- Similar to list but immutable

#Sample Tuple
emails=("x@gmail.com","y@yahoo.com","z@hotmail.com")
print("Tuple Elements:",emails)
print("First element in emails",emails[0])
print("length of Tuples:",len(emails))
updated_emails=emails.__add__(("zz@gmail.com",))
print("Tuple Elements:",emails) # Notice emails is immutable
print("Tuple Elements:",updated_emails)
#emails[0] = "zz@gmail.com" # 'tuple' object does not support item assignment

#Repeting the tuple elements
emails_repeated=emails*2
print("Repeating the tuple elements using *:",emails_repeated)
print("Slicing:",emails[0:2])
#tuple Concatenation
New_emails=emails+emails_repeated
print("New Emails?(Concatenation):",New_emails)

#One element Tuple
one_email=("hr@atos.net",)
print(type(one_email))

#Packing and Unpacking Tuples
(One,Two,three)=(1,2,3)
print("Value of Variable One:",One)
#Python 3
myvalues=(10,20,30,40)
a,*b,c=myvalues
print(a,b,c)

#Converting a list to a Tuple: tuple()
countries=["UK","Russia","USA","Japan","Canada"]
countriesTuple=tuple(countries)
print(countriesTuple)

#Converting from a Tuple to List : list()
TupleToList=list(countriesTuple)
print(TupleToList)

#Tuple of Tuples
numTuple=((2,4,6,8),(3,9,12),(5,15,15,20,25,30))
print("Tuple of Tuples:",numTuple)
#Converting to List
numList=list(numTuple)
print("Tuple of Tuples converted to List:",numList)
mynumList=[]
#For each loop: Creating a list of lists from the tuple of tuples
for nums in numList:
    mynumList.append(list(nums))
print("New List created from Tuple of tuples:", mynumList)
#For each loop: Creating a list from the tuple of tuples
mynumList=[]
for nums in numList:
    mynumList.extend(list(nums))
print("New List created from Tuple of tuples:",mynumList)

