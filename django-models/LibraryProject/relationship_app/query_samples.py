from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
try:
    author = Author.objects.get(name="J.K. Rowling")
    books_by_author = Book.objects.filter(author=author)
except Author.DoesNotExist:
    books_by_author = []
    print("Author not found.")

# 2. List all books in a library
try:
    library = Library.objects.get(name="Central Library")
    books_in_library = library.books.all()
except Library.DoesNotExist:
    books_in_library = []
    print("Library not found.")

# 3. Retrieve the librarian for a library
try:
    librarian = library.librarian  # Uses OneToOneField reverse access
    librarian_name = librarian.name
except (Library.DoesNotExist, Librarian.DoesNotExist, AttributeError):
    librarian_name = "Librarian not found."

# Output the results
print("Books by author:", [book.title for book in books_by_author])
print("Books in library:", [book.title for book in books_in_library])
print("Librarian name:", librarian_name)
