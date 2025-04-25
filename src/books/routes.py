from fastapi import APIRouter, HTTPException, Response, status
from typing import List
from src.books.book_data import books
from src.books.schemas import Book, BookUpdatedModel

book_router = APIRouter()

@book_router.get("/", response_model=List[Book])
async def get_all_books():
    return books

@book_router.post(
    "/", 
    response_model=Book, 
    status_code=status.HTTP_201_CREATED
)
async def create_book(book: Book):
    new_book = book.model_dump()  # Pydantic v2: .model_dump() → dict
    books.append(new_book)
    return new_book

@book_router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int):
    for b in books:
        if b["id"] == book_id:
            return b
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")

@book_router.patch("/{book_id}", response_model=Book)
async def update_book(
    book_id: int, 
    update: BookUpdatedModel
):
    for b in books:
        if b["id"] == book_id:
            data = update.model_dump(exclude_unset=True)
            for key, value in data.items():
                b[key] = value
            return b
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")

@book_router.delete(
    "/{book_id}", 
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book(book_id: int):
    for b in books:
        if b["id"] == book_id:
            books.remove(b)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")
