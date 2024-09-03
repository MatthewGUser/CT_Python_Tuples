# [ Task 1 ]

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Add book being passed a list and item
def add_book(library, new_book):
    if new_book in library:
        print(f"The book '{new_book[0]}' by {new_book[1]} is already in the library.")
    else:
        library.append(new_book)
        print(f"The book '{new_book[0]}' by {new_book[1]} has been added to the library.")
    return library

new_books = [
    ("1984", "George Orwell"),  # Duplicate book
    ("To Kill a Mockingbird", "Harper Lee")  # New book
]

for book in new_books:
    library = add_book(library, book)

print("\nUpdated Library:", library)
