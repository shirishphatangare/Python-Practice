
friends_data_list = input("Enter names of 3 friends (Comma separated): ").casefold().split(',')
friends_data_set = set()

# Removes spaces if any and add to set
for friend in friends_data_list:
    friends_data_set.add(friend.strip())

people_file = open('./resources/people.txt','r')
people_data_list = [line.casefold().strip() for line in people_file.readlines()] # strip each line of newline characters
people_data_set = set(people_data_list)
people_file.close()

# Get common data from friends_data_set and people_data_set (intersection of sets)
friends_nearby_data_set = people_data_set.intersection(friends_data_set)

friends_nearby_file = open('./resources/friends_nearby.txt','w') # with 'w' mode file is created if it does not exist

# Traverse set and write to file
if(len(friends_nearby_data_set) != 0):
    for friend in friends_nearby_data_set:
        friend_capitalized = friend.capitalize()
        print(f"{friend_capitalized} is nearby! Meet up")
        friends_nearby_file.write(f'{friend_capitalized}\n')
else:
    print("Bad luck, No friends nearby!")

friends_nearby_file.close()




