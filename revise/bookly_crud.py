from fastapi import FastAPI, status, Response
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# 🧠 BaseModel used to define request/response schema with validation
class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


# ⚙️ PATCH model with all optional fields (true partial update)
class BookUpdatedModel(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None
    published_date: Optional[str] = None  # included in case we want to update date too


# 📚 In-memory database (just a Python list of dictionaries)
books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English"
    },
    {
        "id": 2,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall",
        "published_date": "2008-08-11",
        "page_count": 464,
        "language": "English"
    },
    {
        "id": 3,
        "title": "You Don't Know JS",
        "author": "Kyle Simpson",
        "publisher": "O'Reilly Media",
        "published_date": "2015-12-27",
        "page_count": 278,
        "language": "English"
    },
    {
        "id": 4,
        "title": "Eloquent JavaScript",
        "author": "Marijn Haverbeke",
        "publisher": "No Starch Press",
        "published_date": "2018-12-04",
        "page_count": 472,
        "language": "English"
    },
    {
        "id": 5,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publisher": "No Starch Press",
        "published_date": "2019-05-03",
        "page_count": 544,
        "language": "English"
    },
    {
        "id": 6,
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media",
        "published_date": "2022-03-01",
        "page_count": 1014,
        "language": "English"
    },
    {
        "id": 7,
        "title": "Grokking Algorithms",
        "author": "Aditya Bhargava",
        "publisher": "Manning Publications",
        "published_date": "2016-05-22",
        "page_count": 256,
        "language": "English"
    },
    {
        "id": 8,
        "title": "The Pragmatic Programmer",
        "author": "Andy Hunt & Dave Thomas",
        "publisher": "Addison-Wesley",
        "published_date": "1999-10-20",
        "page_count": 352,
        "language": "English"
    },
    {
        "id": 9,
        "title": "Design Patterns",
        "author": "Erich Gamma et al.",
        "publisher": "Addison-Wesley",
        "published_date": "1994-10-21",
        "page_count": 395,
        "language": "English"
    },
    {
        "id": 10,
        "title": "Cracking the Coding Interview",
        "author": "Gayle Laakmann McDowell",
        "publisher": "CareerCup",
        "published_date": "2015-07-01",
        "page_count": 687,
        "language": "English"
    }
]


# ✅ GET all books (returns a list of Book models)
@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books


# ✅ POST a new book
@app.post("/books")
async def create_book(book_data: Book) -> dict:
    # 📦 .model_dump() used in Pydantic v2 to convert model to dict
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


# ✅ GET a book by ID
@app.get("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    # 🚨 Raise 404 if not found
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found.")


# ✅ PATCH a book by ID (partial update)
@app.patch("/book/{book_id}")
async def update_book(book_id: int, book_update_data: BookUpdatedModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            # 🧠 Use exclude_unset=True to apply only the fields sent in the request
            update_data = book_update_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                book[key] = value
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found.")


# ✅ DELETE a book by ID
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            # 💡 Return empty response (204 = No Content)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found.")