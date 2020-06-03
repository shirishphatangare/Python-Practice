
# Menu driven application to add, list and find movies

movies = []  # List of dictionaries - Global variable

def menu():

    user_choice = input(
    """                     *** Menu ***
                      -------------------------
                      1) Add a new movie ('a')
                      2) List all movies ('l')
                      3) Find a movie ('f')
                      4) Quit ('q')
                      -------------------------
                      Enter your choice (a/l/f/q): """)

    while(user_choice != 'q'):
        if(user_choice == 'a'):
            add_movie()
        elif(user_choice == 'l'):
            list_movies(movies)
        elif(user_choice == 'f'):
            find_movie()
        else:
            print("Invalid choice. Please try again!")

        user_choice = input(
        """                 *** Menu ***
                      -------------------------
                      1) Add a new movie ('a')
                      2) List all movies ('l')
                      3) Find a movie ('f')
                      4) Quit ('q')
                      -------------------------
                      Enter your choice (a/l/f/q): """)


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
    find_high = input("Please enter what you want to find at high level (name/genere/year): ")
    find_low = input("Please enter what you want to find exactly: ")
    # Show details of found movies
    list_movies(get_found_items(movies, find_low, lambda x:x[find_high])) # lambda returns x['find_high'] of passed parameter x

# Generalization with items
def get_found_items(items, expected_result, finder_function):
    found_items = []
    for item in items:
        if finder_function(item) == expected_result:
            found_items.append(item)
    return found_items


menu()