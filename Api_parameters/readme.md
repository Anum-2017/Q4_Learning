# 🚀 FastAPI – API Parameters

In this section, you will learn how to effectively use and validate different types of parameters in FastAPI. We will cover how to work with **path parameters**, **query parameters**, and **request bodies**, along with leveraging FastAPI’s built-in validation features to ensure accurate and secure data handling.

---

### 🧩 Types of Parameters in FastAPI

FastAPI supports several ways to receive and validate input from the client:

- **Path Parameters**: Dynamic parts of the URL path (e.g., `/items/{item_id}`)
- **Query Parameters**: Appended to the URL after `?` (e.g., `/items?skip=0&limit=10`)
- **Request Body**: Sent in the body of the request (commonly in JSON format)
- **Headers**: Custom HTTP headers included in the request
- **Cookies**: Data sent via the `Cookie` header
- **Form Data**: Fields submitted from HTML forms
- **File Uploads**: Files submitted through forms

---

### 🛠️ Project Setup

**Step 1: Initialize a new project**
```bash
uv init fastdca_p1
cd fastdca_p1
```

Step 2: Create a virtual environment

On macOS/Linux:
```bash
uv venv
source .venv/bin/activate
```

On Windows:
```bash
uv venv
.venv\Scripts\activate
```

Step 3: Install FastAPI

```bash
uv add "fastapi[standard]"
```
---

### 🧪 Code: API Parameters

```python
from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# ✅ Item model for request body validation
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# 🔹 1. Path Parameter with Validation
@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(
        ...,  
        title="Item ID",
        description="A unique ID to identify the item",
        ge=1  
    )
):
    return {"message": "Item fetched successfully", "item_id": item_id}

# 🔹 2. Query Parameters with Validation
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        title="Search Query",
        description="Keyword to search for items",
        min_length=3,
        max_length=50
    ),
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, le=100, description="Maximum number of items to return")
):
    return {
        "message": "Items fetched successfully",
        "query": q,
        "skip": skip,
        "limit": limit
    }

# 🔹 3. Path + Query + Body together (with all validations)
@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),
    q: Optional[str] = Query(None, min_length=3, max_length=50),
    item: Optional[Item] = Body(None, description="JSON body with updated item data")
):
    response = {"item_id": item_id}

    if q:
        response["query"] = q
    if item:
        response["item"] = item.model_dump()

    return {"message": "Item updated successfully", "data": response}
```
---

## ▶️ Run the Server
To start the FastAPI server:

```bash
fastapi dev main.py
```

Open your browser and go to:

```bash
http://localhost:8000/docs
```

This will launch Swagger UI, where you can interact with and test your API endpoints easily.

---

## 🔗 API Endpoints

### GET /items/{item_id}  
Fetch a single item by ID.

**Path parameter:**
- `item_id` (integer ≥ 1)

---

### GET /items/  
Fetch items with optional filters.

**Query parameters:**
- `q`: optional search term (3–50 characters)  
- `skip`: number of items to skip (default: 0)  
- `limit`: max items to return (default: 10)

---

### PUT /items/validated/{item_id}  
Update an item.

**Path parameter:**
- `item_id` (integer ≥ 1)

**Query parameter:**
- `q`: optional search keyword

**Body:**
- `name`: item name (string)  
- `description`: optional item description (string)  
- `price`: item price (float)

--- 

## 📌 Key Points to Keep in Mind

- Use `Path()` to validate path parameters (e.g., `item_id`).
- Use `Query()` to validate query parameters (e.g., `q`, `skip`, `limit`).
- Both `Path()` and `Query()` support powerful validation features:
  - Constraints like `ge` (greater than or equal), `gt` (greater than), `le` (less than or equal), and `lt` (less than) for numerical values.
  - String length validation with `min_length` and `max_length`.
  - Pattern matching using `regex` or `pattern` to ensure input matches specific formats.
  - Restrict possible values using `enum`.
- FastAPI automatically validates the parameters based on the defined rules.
- In case of validation errors, FastAPI will return a `422 Unprocessable Entity` status code with clear and detailed error information.

---

## 🏁 Conclusion

FastAPI makes handling and validating API parameters straightforward with features like Path() and Query(). These tools ensure data integrity by enforcing rules like length, value constraints, and pattern matching. With automatic validation and clear error messages, FastAPI helps you build secure, reliable APIs with minimal effort.

