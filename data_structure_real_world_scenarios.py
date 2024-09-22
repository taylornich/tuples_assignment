# question 2 task 1

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(title, author):
    new_book = (title, author)

    if new_book in library:
        print("This book is already in the library.")
    else:
        library.append(new_book)

book = add_book("Howling Dark", "Christopher Ruocchio")

print(library)