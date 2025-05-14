# === Easy Questions ===

# 1. Basic Class Design
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# 2. Class Methods
class Counter: 
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def reset(self):
        self.value = 0


# === Medium Questions ===

# 1. Inheritance
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, doors, fuel_type):
        super().__init__(make, model, year)
        self.doors = doors
        self.fuel_type = fuel_type


# 2. Encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number


# === Hard Questions ===

# 1. Polymorphism and Abstract Classes
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area method.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):  # Overrides earlier Rectangle
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height, side):
        self.base = base
        self.height = height
        self.side = side

    def area(self):
        return 0.5 * self.base * self.height


# 2. Complex Class Relationships
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.checked_out = {}

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def checkout_book(self, book, member):
        if book in self.books and book not in self.checked_out:
            self.checked_out[book] = member
            member.borrowed_books.append(book)

    def return_book(self, book, member):
        if book in self.checked_out and self.checked_out[book] == member:
            del self.checked_out[book]
            member.borrowed_books.remove(book)

    def is_book_available(self, book):
        return book in self.books and book not in self.checked_out


# === Test Cases ===
if __name__ == "__main__":
    # Rectangle
    rect = Rectangle(5, 10)
    print(rect.area())       
    print(rect.perimeter())  

    # Counter
    counter = Counter()
    counter.increment()
    counter.increment()
    print(counter.value)
    counter.decrement()
    print(counter.value)
    counter.reset()
    print(counter.value)

    # Car
    car = Car("Toyota", "Corolla", 2020, 4, "Gasoline")
    print(car.make)
    print(car.doors)

    # BankAccount
    account = BankAccount("123456", 1000)
    print(account.get_balance())
    account.deposit(500)
    print(account.get_balance())
    account.withdraw(200)
    print(account.get_balance())
    print(account.get_account_number())

    # Shapes
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)

    shapes = [circle, rectangle, triangle]
    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area()}")

    # Library System
    library = Library()
    book1 = Book("Python Programming", "John Smith")
    book2 = Book("Data Structures", "Jane Doe")

    library.add_book(book1)
    library.add_book(book2)

    member = Member("Alice", "M001")
    library.register_member(member)

    library.checkout_book(book1, member)
    print(library.is_book_available(book1))
    print(library.is_book_available(book2))

    library.return_book(book1, member)
    print(library.is_book_available(book1))
