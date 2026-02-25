class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed= True
            return True
        return False
    
    def return_book(self):
        self.is_available = True
        print(f"Buku '{self.title}' telah tersedia di rak.")

class Member:
    def __init__(self, name, member):
        self.name = name
        self.member = member
        self.borrowed_books = []

class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id

class borrowTransaction:
    def __init__(self, book: Book, member: Member, staff: Staff):
        self.book = book
        self.member = member
        self.staff = staff
        self.borrow_date = "2026-02-01"
        self.returned = False
    
    def borrow_book(self):
        if self.book.borrow():
            self.member.borrowed_books.append(self)
            return True
        return False
    
    def return_book(self):
        self.book.return_book()

        self.returned = True
