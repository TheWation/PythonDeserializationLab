from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import pickle
import base64

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

books = [
    {"title": "Python Crash Course", "author": "Eric Matthes", "year": 2019},
    {"title": "Fluent Python", "author": "Luciano Ramalho", "year": 2022},
    {"title": "Effective Python", "author": "Brett Slatkin", "year": 2020}
]

@app.get("/", response_class=HTMLResponse)
def home():
    book_links = "".join(
        f'<li><a href="/book?data={base64.b64encode(pickle.dumps(book)).decode()}">{book["title"]}</a></li>'
        for book in books
    )
    return f"""
    <html>
    <head>
        <title>Python Books</title>
        <link rel="stylesheet" href="/static/styles.css">
    </head>
    <body>
        <div class="container">
            <h1>Books</h1>
            <ul>
                {book_links}
            </ul>
        </div>
    </body>
    </html>
    """

@app.get("/book", response_class=HTMLResponse)
def book_detail(request: Request, data: str):
    decoded_data = pickle.loads(base64.b64decode(data))
    return f"""
    <html>
    <head>
        <title>{decoded_data['title']}</title>
        <link rel="stylesheet" href="/static/styles.css">
    </head>
    <body>
        <div class="container">
            <h1>{decoded_data['title']}</h1>
            <p><strong>Author:</strong> {decoded_data['author']}</p>
            <p><strong>Year:</strong> {decoded_data['year']}</p>
            <a href='/'>Back</a>
        </div>
    </body>
    </html>
    """
