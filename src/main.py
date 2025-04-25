from fastapi import FastAPI
from src.books.routes import book_router

app = FastAPI(
    title="Bookly API",
    version="v1"
)

# Mount the books router under /api/v1/books
app.include_router(
    book_router,
    prefix="/api/v1/books",
    tags=["books"],
)
