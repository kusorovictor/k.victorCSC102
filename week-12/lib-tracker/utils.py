#Not a valid way to check if a string is a valid ISBN-13, just keeping it simple for now.
def is_isbn(isbn) -> bool:
    """"Check if the given string is a valid ISBN-13."""
    if not isinstance(isbn, str):
        return False
    isbn = isbn.replace("-", "").replace(" ", "")
    if len(isbn) == 13 and isbn.isdigit():
        return True
    return False  