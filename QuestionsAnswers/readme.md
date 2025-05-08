# 🚀 FastAPI Project by Anum

This is a simple and beginner-friendly FastAPI project created by **Anum Kamal**. It demonstrates how to set up a basic REST API with FastAPI, including a root route and a dynamic route with optional query parameters.

---

## 📁 Project Files

```
📦 fastapi-anum/
 ┣ 📄 main.py
 ┗ 📄 README.md
```

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **FastAPI**
- **Uvicorn** (ASGI server)

---

## ✅ Installation

1. **Clone this repository** or create a new directory and save the `main.py` file inside it.

2. **Create a virtual environment (optional but recommended)**:

```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3. **Install FastAPI and Uvicorn**:

```bash
pip install fastapi uvicorn
```

---

## ▶️ Running the App

To run the FastAPI app, use the following command:

```bash
uvicorn main:app --reload
```

- `main`: Refers to your Python file `main.py`.
- `app`: The FastAPI app object created in the file.
- `--reload`: Automatically reloads the server on file changes (useful in development).

After running, visit:

- 🌐 `http://127.0.0.1:8000` — Root endpoint
- 📘 `http://127.0.0.1:8000/docs` — Swagger UI
- 📕 `http://127.0.0.1:8000/redoc` — ReDoc documentation

---

## 📦 API Endpoints

### 🔹 1. Root Endpoint

- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns a welcome message.
- **Response**:
```json
{
  "message": "Hello from Anum"
}
```

---

### 🔹 2. Dynamic Item Endpoint

- **URL**: `/items/{item_id}`
- **Method**: `GET`
- **Path Parameter**:
  - `item_id` (integer): ID of the item
- **Query Parameter** (optional):
  - `q` (string): A query string

- **Example URL**:
```
http://127.0.0.1:8000/items/42?q=fastapi
```

- **Example Response**:
```json
{
  "item_id": 42,
  "q": "fastapi"
}
```

---

## 📃 main.py Code

Here is the full code in `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Anum"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

---

## 📘 Features

- FastAPI-based REST API
- Supports path and query parameters
- Built-in documentation with Swagger and ReDoc
- Auto-reload for development

---

## 🧠 About the Author

**Anum Kamal**  
Software Engineer | Backend Developer  
Passionate about learning Python, FastAPI, and building useful tools.  
Always exploring the world of APIs and automation. 🚀

---

## 📌 Notes

- FastAPI is type-safe and auto-generates OpenAPI schemas.
- The `q` parameter in `/items/{item_id}` is optional.
- You can build upon this to include more features like POST requests, database integration, etc.

---

## 📄 License

This project is released under the MIT License.
You are free to use, modify, and distribute this software.

---

## 🧪 1. What is a Virtual Environment?

A **virtual environment** is a self-contained Python environment that allows you to isolate your dependencies and not pollute the global Python environment. It’s a directory that contains a Python interpreter, a library (with its own site-packages directory), and other support files.

**Why use it?**
- Keeps dependencies isolated per project.
- Prevents version conflicts.
- Makes deployment and collaboration easier.

You can create one using:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

---

## 🎯 2. What are Decorators?

**Decorators** are special functions in Python that modify or extend the behavior of other functions without changing their actual code. They're very powerful in adding reusable functionalities like logging, validation, or access control.

FastAPI heavily uses decorators to define API routes.

---

## 💡 3. Example of Decorators in FastAPI

### Code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Anum"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

### Explanation:

1. `from fastapi import FastAPI`: Import the FastAPI class.
2. `app = FastAPI()`: Create an instance of the FastAPI application.
3. `@app.get("/")`: This decorator registers the `read_root` function to handle GET requests at the root URL (`/`).
4. `def read_root()`: Returns a JSON with `{"message": "Hello from Anum"}`.
5. `@app.get("/items/{item_id}")`: Registers a route that accepts an integer `item_id` in the URL path.
6. `def read_item(item_id: int, q: str | None = None)`: 
   - `item_id`: a required path parameter (int).
   - `q`: an optional query parameter (string or None).
7. `return {"item_id": item_id, "q": q}`: Returns both values as a dictionary.

---

### 🔍 Example Use Cases

1. Root URL:
   ```
   http://localhost:8000/
   ```
   **Response:**
   ```json
   {"message": "Hello from Anum"}
   ```

2. With item ID:
   ```
   http://localhost:8000/items/123
   ```
   **Response:**
   ```json
   {"item_id": 123, "q": null}
   ```

3. With item ID and query:
   ```
   http://localhost:8000/items/123?q=hello
   ```
   **Response:**
   ```json
   {"item_id": 123, "q": "hello"}
   ```

This example shows how FastAPI uses decorators for API routing and how both path and query parameters work together.

---
