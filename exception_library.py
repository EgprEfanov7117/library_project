
class LibraryError(Exception):
    pass

# ===== Book =====
class BookNotFound(LibraryError):
    pass

class EmptyBookTitleError(LibraryError):
    pass


# ===== Author =====
class AuthorNotFound(LibraryError):
    pass
class EmptyNameError(LibraryError):
    pass
class EmptyCountryError(LibraryError):
    pass


# ===== Publisher =====
class PublisherNotFound(LibraryError):
    pass