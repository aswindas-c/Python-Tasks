class Book:
    #title author and unique book id
    def __init__(self,book_id,title,author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
    def display_book(self):
        print(f"Book Id : {self.book_id}\n"
              f"Book Title : {self.title}\n"
              f"Book Author : {self.author}")
class Library:
    #holds collection of books
    def __init__(self):
        self.books = {}
    def add_book(self,book):
        self.books[book.book_id] = book
    def get_book_by_id(self,book_id) -> Book:
        if self.books.get(book_id) is None:
            raise KeyError("Book not found")
        else:
            return self.books.get(book_id)
    def remove_book(self,book_id):
        del self.books[book_id]
        print(f"Book with id {book_id} removed successfully")
    def search_book(self,partial_title):
        searched_book = [book.title for book in self.books.values() if book.title.startswith(partial_title)]
        if not searched_book:
            raise ValueError("Searched Book Not Found")
        else:
            print("Searched Books : \n")
            for i in searched_book:
                print(i)
    #generator to yield books details
    def get_books(self):
        for book in self.books.values():
            if book.available:
                yield book
class User:
    #name and unique user id
    def __init__(self,user_name,user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.borrowed = {}
    def display_user(self,user_id):
        print(f"User ID : {self.user_id}")
        print(f"Name : {self.user_name}")
class LibraryUser(User):
    def __init__(self, user_name, user_id):
        super().__init__(user_name, user_id)
        self.user_name = user_name
        self.user_id = user_id
        self.borrowed[self.user_id] = []
    def borrow_book(self,book_id,user_id,borrow):
        self.borrowed[user_id].append(borrow)
        print("Book Borrowed Successfully")
    def return_book(self,book_id,user_id,title):
        self.borrowed[user_id].remove(title)
        print("Book Returned Successfully")
    def track_book(self,user_id):
        print(f"Books Borrowed by {self.user_name}")
        if len(self.borrowed[user_id]) != 0:
            for i in self.borrowed[user_id]:
                print(i)
        else:
            print("No books borrowed else to return")