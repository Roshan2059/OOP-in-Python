class Library:
    def __init__(self):
        self.no_books = 0
        self.books = []
    def add_book(self, book_title):
        self.books.append(book_title)
        self.no_books += 1
    def show_books(self):
        for i in self.books:
            print(i)
    def no_of_books(self):
        print(f"You have {self.no_books} books in your library")

l1 = Library()
l1.add_book("JAVA")
l1.add_book("python")
l1.add_book("C")
l1.add_book("C++")
l1.show_books()
l1.no_of_books()

#Yo program bataa maile k sikey vandaa kheri kunai pani variable ra method ko name chai same hu hudo rainaxa...