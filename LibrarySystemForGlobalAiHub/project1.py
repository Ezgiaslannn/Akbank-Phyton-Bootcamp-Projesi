class Library:
    def _init_(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def _del_(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        for book in books:
            book_info = book.strip().split(',')
            print(f"Book Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        book_first_release_year = input("Enter first release year: ")
        book_number_of_pages = input("Enter number of pages: ")
        information_of_the_book = f"{book_title},{book_author},{book_first_release_year},{book_number_of_pages}\n"

        self.file.write(information_of_the_book)
        print(f"{book_title} added to the library.")

    def remove_book(self):
        
        user_response = input(f"Do you want to remove any book from the library? (yes/no): ").lower()
        book_title_to_remove = input("Enter the title of the book to remove: ")

        if user_response in ["yes", "y"]:
            self.file.seek(0)
            lines = self.file.readlines()
            self.file.seek(0)
            self.file.truncate()

            removed = False
            for line in lines:
                if book_title_to_remove not in line:
                    self.file.write(line)
                else:
                    removed = True

            if removed:
                print(f"{book_title_to_remove} removed from the library.")
            else:
                print(f"{book_title_to_remove} not found in the library.")
        else:
            print(f"{book_title_to_remove} was not removed from the library.")

# Test the Library class
library = Library()
library.add_book()
library.list_books()
library.remove_book()
library.list_books()