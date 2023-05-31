"""
    SOLID Principle (Design pattern) implemented in code for proper explanation
"""

# Single Responsibility Principle (SRP)
class Customer:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class CustomerPersistence:
    def save(self, customer):
        # Code to persist customer object
        pass

# Open-Closed Principle (OCP)
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Liskov Substitution Principle (LSP)
class Vehicle:
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Bicycle(Vehicle):
    def start_engine(self):
        raise NotImplementedError("Bicycles don't have engines")

# Interface Segregation Principle (ISP)
class Printer:
    def print_document(self, document):
        pass

class Scanner:
    def scan_document(self):
        pass

class MultiFunctionDevice(Printer, Scanner):
    def print_document(self, document):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")

# Dependency Inversion Principle (DIP)
class Logger:
    def log(self, message):
        print("Logging:", message)

class UserManager:
    def __init__(self, logger):
        self.logger = logger

    def create_user(self, username):
        # Code to create a new user
        self.logger.log("User created: " + username)

logger = Logger()
user_manager = UserManager(logger)
user_manager.create_user("John Doe")
