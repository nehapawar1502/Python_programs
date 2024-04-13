class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []
        
    def addBook(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)
        
    def showInfo(self):
        print(f"The library has {self.no_of_books} books, the books are:")
        for book in self.books:
            print(book)
        
    
l1 = Library()
l1.addBook("Harry potter")
l1.addBook("Harry potter-1")
l1.addBook("Harry potter-2")
l1.addBook("Harry potter-3")
l1.showInfo()
        