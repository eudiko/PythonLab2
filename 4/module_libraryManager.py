library = {}

def add_book(isbn, title, author, publisher, volume, year, isbn_number):
    library[isbn] = {
        'title': title,
        'author': author,
        'publisher': publisher,
        'volume': volume,
        'year': year,
        'isbn_number': isbn_number
    }

def remove_book(isbn):
    if isbn in library:
        del library[isbn]
        return True
    return False

def get_book_details(isbn):
    return library.get(isbn, None)

def search_books_by_title(title):
    return [book for book in library.values() if title.lower() in book['title'].lower()]

def search_books_by_author(author):
    return [book for book in library.values() if author.lower() in book['author'].lower()]

def list_all_books():
    return list(library.values())

def update_book_details(isbn, title=None, author=None, publisher=None, volume=None, year=None, isbn_number=None):
    if isbn in library:
        if title:
            library[isbn]['title'] = title
        if author:
            library[isbn]['author'] = author
        if publisher:
            library[isbn]['publisher'] = publisher
        if volume:
            library[isbn]['volume'] = volume
        if year:
            library[isbn]['year'] = year
        if isbn_number:
            library[isbn]['isbn_number'] = isbn_number
        return True
    return False

def is_book_available(isbn):
    return isbn in library
