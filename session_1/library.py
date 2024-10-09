books = []
users = []


def add_user(name):
    users.append({"name": name, "borrowed_books": []})
    return True


def add_book(title, author):
    books.append({"title": title, "author": author, "available": True})
    return True


def borrow_book(user_name, title):
    user = find_user(user_name)
    if not user:
        return False

    for book in books:
        if book["title"] == title and book["available"]:
            book["available"] = False
            user["borrowed_books"].append(title)
            return True

    return False


def return_book(user_name, title):
    user = find_user(user_name)
    if not user:
        return False

    if title in user["borrowed_books"]:
        user["borrowed_books"].remove(title)
        for book in books:
            if book["title"] == title:
                book["available"] = True
                return True

    return False


def find_user(name):
    for user in users:
        if user["name"] == name:
            return user
    return None


def list_books():
    book_list = []
    for book in books:
        status = "available" if book["available"] else "borrowed"
        book_list.append(f"{book['title']} by {book['author']} - {status}")
    return book_list
