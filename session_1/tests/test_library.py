from session_1.library import add_book, add_user, books, users, borrow_book, return_book, find_user, list_books


def test_add_user():
    # given
    # User does not exist
    # when
    result = add_user("Alice")
    # then
    assert result is True
    assert len(users) == 1
    assert users[0]['name'] == "Alice"
    assert users[0]['borrowed_books'] == []


def test_add_book():
    # given
    # Book does not exist
    # when
    result = add_book("1984", "George Orwell")
    # then
    assert result is True
    assert len(books) == 1
    assert books[0]['title'] == "1984"
    assert books[0]['author'] == "George Orwell"
    assert books[0]['available'] is True


def test_borrow_book_success():
    # given
    add_user("Alice")
    add_book("1984", "George Orwell")
    # when
    result = borrow_book("Alice", "1984")
    # then
    assert result is True
    assert books[0]['available'] is False
    assert "1984" in users[0]['borrowed_books']


def test_borrow_book_user_not_found():
    # given
    add_book("1984", "George Orwell")
    # when
    result = borrow_book("NonExistentUser", "1984")
    # then
    assert result is False
    assert books[0]['available'] is True


def test_borrow_book_book_not_available():
    # given
    add_user("Alice")
    add_user("Bob")
    add_book("1984", "George Orwell")
    borrow_book("Alice", "1984")
    # when
    result = borrow_book("Bob", "1984")
    # then
    assert result is False
    assert books[0]['available'] is False
    assert "1984" not in users[1]['borrowed_books']


def test_return_book_success():
    # given
    add_user("Alice")
    add_book("1984", "George Orwell")
    borrow_book("Alice", "1984")
    # when
    result = return_book("Alice", "1984")
    # then
    assert result is True
    assert books[0]['available'] is True
    assert "1984" not in users[0]['borrowed_books']


def test_return_book_user_not_found():
    # given
    add_book("1984", "George Orwell")
    # when
    result = return_book("NonExistentUser", "1984")
    # then
    assert result is False
    assert books[0]['available'] is True


def test_return_book_not_borrowed_by_user():
    # given
    add_user("Alice")
    add_user("Bob")
    add_book("1984", "George Orwell")
    borrow_book("Alice", "1984")
    # when
    result = return_book("Bob", "1984")
    # then
    assert result is False
    assert books[0]['available'] is False
    assert "1984" in users[0]['borrowed_books']


def test_find_user():
    # given
    add_user("Alice")
    # when
    user = find_user("Alice")
    # then
    assert user is not None
    assert user['name'] == "Alice"


def test_find_user_not_found():
    # given
    # No user exists
    # when
    user = find_user("NonExistentUser")
    # then
    assert user is None


def test_list_books():
    # given
    add_book("1984", "George Orwell")
    add_book("The Great Gatsby", "F. Scott Fitzgerald")
    # when
    result = list_books()
    # then
    assert result == [
        "1984 by George Orwell - available",
        "The Great Gatsby by F. Scott Fitzgerald - available"
    ]
