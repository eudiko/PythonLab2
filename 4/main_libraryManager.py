import module_libraryManager as lm

def main():
    books = [
        ("978-0134685991", "Operating System Concepts", "Abraham Silberschatz", "Wiley", "10th", 2020, "978-0134685991"),
        ("978-0135166307", "Data Structures and Algorithm Analysis in C++", "Mark Allen Weiss", "Pearson", "4th", 2021, "978-0135166307"),
        ("978-1449355739", "Introduction to Machine Learning with Python", "Andreas C. Müller", "O'Reilly Media", "1st", 2022, "978-1449355739"),
        ("978-0134092669", "Modern Operating Systems", "Andrew S. Tanenbaum", "Pearson", "4th", 2020, "978-0134092669"),
        ("978-1492041139", "Machine Learning for Beginners", "Chris Sebastian", "O'Reilly Media", "1st", 2023, "978-1492041139"),
        ("978-0262046305", "Designing Data-Intensive Applications", "Martin Kleppmann", "MIT Press", "1st", 2021, "978-0262046305"),
        ("978-1119700910", "Operating Systems: Internals and Design Principles", "William Stallings", "Pearson", "9th", 2020, "978-1119700910"),
        ("978-0135166284", "Data Structures and Problem Solving Using Java", "Mark Allen Weiss", "Pearson", "4th", 2022, "978-0135166284"),
        ("978-1492056740", "Machine Learning Engineering", "Andriy Burkov", "O'Reilly Media", "1st", 2022, "978-1492056740"),
        ("978-0135178195", "Operating Systems: Three Easy Pieces", "Remzi H. Arpaci-Dusseau", "CreateSpace", "1st", 2021, "978-0135178195"),
        ("978-1492070982", "Data Structures and Algorithms in Python", "Michael T. Goodrich", "Wiley", "1st", 2020, "978-1492070982"),
        ("978-1492032645", "Machine Learning with Python Cookbook", "Chris Albon", "O'Reilly Media", "1st", 2021, "978-1492032645"),
        ("978-0321751041", "Operating Systems: Principles and Practice", "Thomas Anderson", "Pearson", "2nd", 2020, "978-0321751041"),
        ("978-0134670948", "Data Structures and Algorithms in Java", "Robert Lafore", "Pearson", "3rd", 2023, "978-0134670948"),
        ("978-1449369415", "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", "Aurélien Géron", "O'Reilly Media", "2nd", 2022, "978-1449369415"),
        ("978-0136031953", "Understanding the Linux Kernel", "Daniel P. Bovet", "O'Reilly Media", "3rd", 2020, "978-0136031953"),
        ("978-1492051367", "Data Structures and Algorithms Using Python", "Rance D. Necaise", "Wiley", "1st", 2021, "978-1492051367"),
        ("978-1492052210", "Practical Machine Learning with Python", "Dipanjan Sarkar", "Apress", "1st", 2022, "978-1492052210"),
        ("978-0321967445", "Linux System Programming", "Robert Love", "O'Reilly Media", "2nd", 2020, "978-0321967445"),
        ("978-0134463971", "Data Structures and Algorithms Made Easy in Java", "Narasimha Karumanchi", "CareerMonk Publications", "2nd", 2021, "978-0134463971"),
        ("978-1492072249", "Machine Learning with Python for Everyone", "Mark Fenner", "Addison-Wesley", "1st", 2022, "978-1492072249"),
        ("978-0135220350", "Understanding Operating Systems", "Ann McIver McHoes", "Cengage Learning", "8th", 2020, "978-0135220350"),
        ("978-1449358655", "Data Structures and Algorithms in JavaScript", "Michael McMillan", "O'Reilly Media", "1st", 2020, "978-1449358655"),
        ("978-0134685991", "Machine Learning Yearning", "Andrew Ng", "Self-Published", "1st", 2022, "978-0134685991"),
        ("978-0131103627", "Operating Systems: A Concept-Based Approach", "D. M. Dhamdhere", "McGraw Hill", "1st", 2021, "978-0131103627")
    ]

    for isbn, title, author, publisher, volume, year, isbn_number in books:
        lm.add_book(isbn, title, author, publisher, volume, year, isbn_number)

    print("All books in the library:")
    for book in lm.list_all_books():
        print(book)

    isbn = "978-0134685991"
    print(f"\nDetails of the book with ISBN {isbn}:")
    print(lm.get_book_details(isbn))

    title = "Operating System"
    print(f"\nBooks with '{title}' in the title:")
    for book in lm.search_books_by_title(title):
        print(book)

    author = "Mark Allen Weiss"
    print(f"\nBooks by '{author}':")
    for book in lm.search_books_by_author(author):
        print(book)

    isbn = "978-0134685991"
    print(f"\nIs the book with ISBN {isbn} available?")
    print(lm.is_book_available(isbn))

    isbn = "978-0134685991"
    print(f"\nUpdating the title of the book with ISBN {isbn}...")
    lm.update_book_details(isbn, title="Operating System Concepts, Updated Edition")
    print(lm.get_book_details(isbn))

    isbn = "978-0131103627"
    print(f"\nRemoving the book with ISBN {isbn}...")
    print(lm.get_book_details(isbn))
    lm.remove_book(isbn)
    print(lm.get_book_details(isbn))

if __name__ == "__main__":
    main()
