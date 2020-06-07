import practice.digital_library_csv_interface as database

USER_CHOICE = """           
        *** Menu ***
-------------------------
1) Add a new book ('A')
2) List all books ('L')
3) Make a book as Read ('R')
4) Delete a book ('D')
5) Quit ('Q')
-------------------------
Enter your choice (A/L/R/D/Q):  """


def menu():
    user_choice = input(USER_CHOICE)

    while user_choice.upper() != 'Q':
        if user_choice.upper() == 'A':
            add_book()
        elif user_choice.upper() == 'L':
            list_all_books()
        elif user_choice.upper() == 'R':
            mark_book_as_read()
        elif user_choice.upper() == 'D':
            delete_book()
        else:
            print("Invalid choice, please enter correct choice (A/L/R/D/Q)")

        user_choice = input(USER_CHOICE)


def add_book():
    book_name = input("Please enter a book name: ")
    book_author = input("Please enter author of the book: ")
    book_item = {'name': book_name, 'author': book_author, 'read': '0'}
    database.insert_record(book_item)


def list_all_books():
    books = database.get_all_records()

    for book in books:
        read = 'YES' if int(book['read']) else 'NO'
        print(f"Name: {book['name']} Author: {book['author']} Read: {read}")


def mark_book_as_read():
    book_name = input("Please enter a book name to mark as read: ")
    database.update_record(book_name)


def delete_book():
    book_name = input("Please enter a book name to delete: ")
    database.delete_record(book_name)

database.create_library_database()
menu()