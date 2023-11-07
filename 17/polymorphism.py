class LibraryItem:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year
        self.is_available = True  # assuming the item is available when created
        
    def get_info(self):
        return f"{self.title} by {self.author}, {self.published_year}"
    
    def check_availability(self):
        return self.is_available


class Book(LibraryItem):
    def __init__(self, title, author, published_year, genre):
        super().__init__(title, author, published_year)
        self.genre = genre
        
    def get_info(self):
        return f"{self.title} by {self.author}, {self.published_year}, Genre: {self.genre}"
    
    def check_availability(self):
        return f"Book availability: {self.is_available}"



class EBook(Book):
    def __init__(self, title, author, published_year, genre, file_size):
        super().__init__(title, author, published_year, genre)
        self.file_size = file_size
        
    def check_availability(self):
        return f"EBook availability: {self.is_available}"

class Audiobook(Book):
    def __init__(self, title, author, published_year, genre, duration):
        super().__init__(title, author, published_year, genre)
        self.duration = duration
    
    def get_info(self):
        return f"{self.title} by {self.author}, {self.published_year}, Genre: {self.genre}, Duration: {self.duration} hours"
    
    def check_availability(self):
        return f"Audiobook availability: {self.is_available}"

class Magazine(LibraryItem):
    def __init__(self, title, author, published_year, issue_number):
        super().__init__(title, author, published_year)
        self.issue_number = issue_number
    
    def get_info(self):
        return f"{self.title} by {self.author}, {self.published_year}, Issue Number: {self.issue_number}"

class Newspaper(LibraryItem):
    def __init__(self, title, author, published_year, edition):
        super().__init__(title, author, published_year)
        self.edition = edition
    
    def get_info(self):
        return f"{self.title} by {self.author}, {self.published_year}, Edition: {self.edition}"

# Creating objects
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
ebook1 = EBook("1984", "George Orwell", 1949, "Dystopian", "2MB")
audiobook1 = Audiobook("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction", "5")

# Testing methods
print(book1.get_info())  # Output: To Kill a Mockingbird by Harper Lee, 1960, Genre: Fiction
print(book1.check_availability())  # Output: Book availability: True
print(ebook1.get_info())  # Output: 1984 by George Orwell, 1949, Genre: Dystopian
print(ebook1.check_availability())  # Output: EBook availability: True
print(audiobook1.get_info())  # Output: The Great Gatsby by F. Scott Fitzgerald, 1925, Genre: Fiction, Duration: 5 hours
print(audiobook1.check_availability())  # Output: Audiobook availability: True
