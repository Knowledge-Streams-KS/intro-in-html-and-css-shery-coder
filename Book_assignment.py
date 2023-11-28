# title: The title of the book.
# author: The author of the book.
# genre: The genre or category of the book.
# price: The price of the book.
# quantity: The number of copies available in the inventory.
class Book:
    def __init__(self, title, author, genre, price, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity

class Bookstore:
    books = []
    def add_book(self,book):
        self.books.append(book)
    def search_by_author(self,author):
        found = False
        for book in self.books:
            if book.author == author:
                print(book.title, book.author, book.genre, book.price, book.quantity)
                found = True 
        if not found:
            print("Book not found")
    def search_by_title(self, title):
        found = False
        for book in self.books:
            if book.title ==title:
                print("Name: ",book.title, "\nAuthor: ",book.author, "\nGenre: ", book.genre, "\nPrice: ",book.price, "\nQuantity: ",book.quantity, "\n")
                found = True
        if not found:
            print("title not found")    
    def remove_book(self, i):
         for book in self.books:
            if book.title.lower() == i.lower():
                # self.books.remove(book)
                if book.quantity <= 0:
                    return None
                copy = Book(book.title, book.author, book.genre, book.price, 1)
                book.quantity -= 1
                return copy
    def display_books(self):
        for book in self.books:
            print("Name: ",book.title, "\nAuthor: ",book.author, "\nGenre: ", book.genre, "\nPrice: ",book.price, "\nQuantity: ",book.quantity, "\n")
class User():
    books_collection = {}
    def __init__(self, name, age, address):
        self.name =  name
        self.age = age 
        self.address = address
    def book_in_bucket(self, book):
        if book.title in self.books_collection:
            d = self.books_collection[book.title]
            d.quantity += 1
            self.books_collection.update({book.title:d})
        else:
            self.books_collection.update({book.title:book})
    def individual_book_bucket(self):
        for title, book in self.books_collection.items():
            print("Name: ",book.title, "\nAuthor: ",book.author, "\nGenre: ", book.genre, "\nPrice: ",book.price, "\nQuantity: ",book.quantity, "\n")

c = Bookstore()
d = Book("junglebook", "mike", "adventure", 200, 3)
d1 = Book("Harry potter", "jerry", "adventure", 200, 500)
d2 = Book("Iron man", "luke", "adventure", 200, 500)
d3 = Book("toy story", "jerry", "adventure", 200, 500)
c.add_book(d)
c.add_book(d1)
c.add_book(d2)
c.add_book(d3)
while(1):
   
    print("Select from the following options: ","\n 1. Add a new book","\n 2. Remove a book",
           "\n 3. Search a book by title", "\n 4. Search a book by author",
            "\n 5. Display the list of books in the inventory", "\n 6. Quit the program.","\n 7.Buy a book","\n\n" )
    inp = input("Enter the number of the task to be performed: ")
    if (inp == "1"):
        name = input("Name of the book: ")
        author = input("\nAuthor of the book: ")
        genre = input("\nGenre of the book: ")
        price = input("\nPrice of the book: ")
        quantity = input("\nQuantity of the book: ")
        d = Book(name, author, genre, price, quantity)
        c.add_book(d)
    if (inp == "2"):
        r = input("\nEnter the title of the book to be removed: ")
        c.remove_book(r)
    if (inp == "3"):
        t = input("Enter the title of the book:")
        c.search_by_title(t)
    if (inp == "4"):
        a = "Enter the author of the book:"
        c.search_by_title(a)
    if (inp == "5"):
        c.display_books()
    if (inp == "6"):
        break
    if (inp == "7"):        
        name = input("\nEnter your name: ")
        age = input("\nEnter your age: ")
        address = input("\nEnter your address: ")
        u = User(name, age, address)
        print("\n")
        c.display_books()
        p = input("\nEnter the title of the book to be purchased:")
        for i in c.books:
            if p == i.title:
                u_book=c.remove_book(p)
                u.book_in_bucket(u_book)
        
        print("\nThe following books have been added:\n") 
        u.individual_book_bucket()

# class Books:
#     def __init__(self, books):
#         for key, value in books.items():
#             setattr(self, key, value)

# class Bookstore:
#     book = {}

#     def Add_Book(self, a):
#         self.book["1"].append(a)

#     def show_Book(self):
#         for k, v in self.book.items():
#             print(k, v)
#     def Remove_Book(self,b):
#         self.book.remove(b)
        # books = {self.title : title,
        # self.genre : genre,
        # self.author : author,
        # self.price : price,
        # self.quantity : quantity}

# my_book = {'name': 'Hero', 'genre': 'motivational', 'author': 'Rhonda Byrne', 'price': 300, 'quantity': 500}

# book = Book(my_book)

# print(book.name, book.genre)

# new_book = Bookstore()

# new_book.Add_Book(book)

# new_book.show_Book(my_book)
# # new_book.Add_Book("cinderalla")



# print(new_book.book)

# class Bookstore:
#     book = []

#     def Add_Book(self,a):
#         self.book.append(a)
#     def Remove_Book(self,b):
#         self.book.remove(b)
#     def search_by_author(author):
#         for i in Bookstore.book:
#             if Bookstore.book[i] == author:
#                 print(Bookstore.book[i])
#     def search_by_title(title):
#         for i in Bookstore.book:
#             if Bookstore.book[i] == title:
#                 print(Bookstore.book[i])