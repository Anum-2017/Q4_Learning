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


