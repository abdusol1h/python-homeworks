# Custom Exceptions
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

# Member Class
class Member:
    MAX_BORROW_LIMIT = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= Member.MAX_BORROW_LIMIT:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than {Member.MAX_BORROW_LIMIT} books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"The book '{title}' is not available in the library.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found.")
            return

        try:
            book = self.find_book(book_title)
            member.borrow_book(book)
            print(f"'{book_title}' borrowed by {member_name}.")
        except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(f"Error: {e}")

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            print(f"Member '{member_name}' not found.")
            return

        try:
            book = self.find_book(book_title)
            member.return_book(book)
            print(f"'{book_title}' returned by {member_name}.")
        except BookNotFoundException:
            print(f"Error: The book '{book_title}' was not found in the library.")

# Testing
library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("Brave New World", "Aldous Huxley"))

member = Member("Alice")
library.add_member(member)

library.borrow_book("Alice", "1984")
library.borrow_book("Alice", "Brave New World")
library.return_book("Alice", "1984")