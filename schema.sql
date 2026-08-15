CREATE TABLE authors (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    birth_year INTEGER,
    country TEXT
);


CREATE TABLE publishers (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL
);


CREATE TABLE books_join (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT NOT NULL,
    isbn TEXT,
    pages INTEGER CHECK (pages > 0),
    price NUMERIC(10, 2) CHECK (price >= 0),
    published_at DATE,
    is_available BOOLEAN DEFAULT TRUE,
    author_id INTEGER,
    publisher_id INTEGER,

    CONSTRAINT books_join_author_id_fkey
        FOREIGN KEY (author_id)
        REFERENCES authors(id),

    CONSTRAINT books_join_publisher_fk
        FOREIGN KEY (publisher_id)
        REFERENCES publishers(id)
);