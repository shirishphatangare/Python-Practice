
# Menu driven application to add, list and find movies

movies = []  # List of dictionaries - Global variable

USER_CHOICE = """           
        *** Menu ***
-------------------------
1) Add a new movie ('A')
2) List all movies ('L')
3) Find a movie ('F')
4) Quit ('Q')
-------------------------
Enter your choice (A/L/F/Q):  """


def menu():
    user_choice = input(USER_CHOICE)

    while(user_choice.upper() != 'Q'):
        if(user_choice.upper() == 'A'):
            add_movie()
        elif(user_choice.upper() == 'L'):
            list_movies(movies)
        elif(user_choice.upper() == 'F'):
            find_movie()
        else:
            print("Invalid choice. Please try again (A/L/F/Q)")

        user_choice = input(USER_CHOICE)


def add_movie():
    name = input("Enter name of a movie: ")
    genere = input("Enter genere of a movie: ")
    year = input("Enter release year of a movie: ")

    # Each movie is a dictionary
    movie = {
             'name':name,
             'genere':genere,
             'year':year
            }
    # Add to movies
    movies.append(movie)


def list_movies(movies):
    if movies is not None:
        for movie in movies:
            print('-' * 20)
            show_item_details(movie)
            print('-' * 20)


# Generalization with item
def show_item_details(item):
    print(f"name: {item['name']}")
    print(f"genere: {item['genere']}")
    print(f"year: {item['year']}")


def find_movie():
    # casefold() used for case-insensitivity
    find_high = input("Please enter what you want to find at high level (name/genere/year): ").casefold()
    find_low = input("Please enter what you want to find exactly: ").casefold()
    # Show details of found movies
    list_movies(get_found_items(movies, find_low, lambda x:x[find_high])) # lambda returns x[find_high] of passed parameter x - find_high can be str or int like x[index]


# Generalization with items
def get_found_items(items, expected_result, finder_function):
    # Method 1 - Using for loop
    found_items = []
    try:
        for item in items:
            if finder_function(item) == expected_result.casefold():
                found_items.append(item)
    except KeyError:
        print("Wrong entry, please enter correct choice (name/genere/year) ")
    return found_items

    # Method 2 - Using list comprehension
    # try:
    #     return [item for item in items if finder_function(item) == expected_result.casefold()]
    # except KeyError:
    #     print("Wrong entry, please enter correct choice (name/genere/year) ")

menu()