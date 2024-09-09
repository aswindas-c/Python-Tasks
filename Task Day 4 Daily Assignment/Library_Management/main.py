import library_module as lm
class Main:

    #exceptions handle
    lib = lm.Library()
    book_id_counter = 1
    user_id_counter = 1
    users ={}
    user_instances = {}
    try:
        while True:
            print("1.Add a book")
            print("2.Remove A book")
            print("3.Create a User")
            print("4.Print Available Books with generator ")
            print("5.Display A book")
            print("6.Search Book")
            print("7.User Functionalities")
            print("8.Exit")
            try:
                choice = int(input())
                if choice == 1:
                    book_title = input("Enter Book name ")
                    author = input("Enter Book author ")
                    book_id = book_id_counter
                    book_id_counter += 1
                    book = lm.Book(book_id,book_title,author)
                    lib.add_book(book)
                elif choice == 2:
                    try:
                        book_id = int(input("Enter Book id "))
                        if book_id not in lib.books.keys():
                            raise KeyError("Book not exist")
                        else:
                            lib.remove_book(book_id)
                    except KeyError as e:
                        print(f"Error : {e}")
                    except ValueError as e:
                        print(f"Error : Enter Integer Book id")
                elif choice == 3:
                    name = input("Enter Username : ")
                    user_id = user_id_counter
                    user = lm.LibraryUser(name,user_id)
                    user_instances[user_id] = user
                    users[user_id] = name
                    print(f"User created with User id : {user_id}")
                    user_id_counter += 1
                elif choice == 4:
                    books = lib.get_books()
                    book_iterator = iter(books)
                    book = next(book_iterator)
                    print(f"Title : {book.title} Author : {book.author}")
                    while True:
                        print("\n1. Next Book")
                        print("2. Quit")
                        choice = input("Enter your choice: ")
                        if choice == "1":
                            try:
                                book = next(book_iterator)
                                print(f"Title : {book.title} Author : {book.author}")
                            except StopIteration:
                                print("No more books available.")
                                break
                        elif choice == "2":
                            break
                        else:
                            print("Invalid choice. Please try again.")
                elif choice == 5:
                    try:
                        book_id = int(input("Enter Book id "))
                        book = lib.get_book_by_id(book_id)
                        book.display_book()
                    except ValueError:
                        print(f"Error : Enter Integer Book id")
                    except KeyError as e:
                        print(f"Error : {e}")

                elif choice == 6:
                    try:
                        partial_title = input("Enter partial title : ")
                        lib.search_book(partial_title)
                    except ValueError as e:
                        print(f"Error : {e}")
                elif choice == 7:
                    try:
                        user_id = int(input("Enter User id : "))
                        if user_id in users.keys():
                            user = user_instances[user_id]
                            while True:
                                print("1.Borrow a Book")
                                print("2.Return A Book")
                                print("3.Track Borrowed Books")
                                print("4.Display User Details")
                                print("5.Back to Main Menu")
                                try:
                                    choice = int(input())
                                    if choice == 1:
                                        try:
                                            book_id = int(input("Enter Book id : "))
                                            if book_id not in lib.books:
                                                print("Book Not available")
                                            else:
                                                if not lib.books[book_id].available:
                                                    print("The Book is already borrowed")
                                                else:
                                                    lib.books[book_id].available = False
                                                    borrow = lib.books[book_id].title
                                                    user.borrow_book(book_id,user_id,borrow)
                                        except ValueError:
                                            print("Enter Integer Book Id")
                                    elif choice == 2:
                                        try:
                                            book_id = int(input("Enter Book id to return : "))
                                            if book_id not in lib.books:
                                                print("Book is not from this Library")
                                            elif lib.books[book_id].title not in user.borrowed[user_id]:
                                                print("You have not borrowed that book to return")
                                            else:
                                                lib.books[book_id].available = True
                                                title = lib.books[book_id].title
                                                user.return_book(book_id, user_id,title)
                                        except ValueError:
                                            print("Enter Integer Book Id")
                                    elif choice == 3:
                                        user.track_book(user_id)
                                    elif choice == 4:
                                        user.display_user(user_id)
                                    elif choice == 5:
                                        break
                                except Exception as e:
                                    print(f"Error : {e}")
                        else:
                            print(f"User with {user_id} does not exist")
                    except ValueError:
                        print("Enter Integer User Id")
                elif choice == 8:
                    exit()
            except ValueError:
                print("Enter Valid Input!!")
    except Exception as e:
        print(f"Error : {e}")
