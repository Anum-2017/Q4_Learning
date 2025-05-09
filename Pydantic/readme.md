# 📦 Pydantic Overview

**Pydantic** is a powerful Python library used for **data validation** and **settings management** using Python type annotations. It enforces type hints at runtime and provides user-friendly error messages.

Pydantic is widely adopted in modern Python frameworks like **FastAPI** for parsing, validating, and serializing data.

---

## ✨ Key Features

- ✅ **Data Validation**  
  Automatically validates input data against defined Python types and structures.

- 📦 **Data Parsing**  
  Parses input data into Python objects, including nested models.

- 🧾 **Type Hints Enforcement**  
  Uses Python's `typing` module (e.g., `List`, `Optional`, `Dict`).

- 🔄 **Serialization/Deserialization**  
  Converts between Python objects and JSON-compatible data easily.

- ⚙️ **Settings Management**  
  Manage app settings with environment variables using `BaseSettings`.

- 📤 **Clear Error Messages**  
  Provides detailed and structured error feedback for invalid data.

- 🔁 **Recursive Models Support**  
  Supports nested and recursive data models seamlessly.

- 🛠️ **ORM Mode**  
  Integrates with ORMs (like SQLAlchemy) via ORM parsing support.

---

## 🚀 Why Use Pydantic in APIs?

- 🧬 **FastAPI Compatibility**  
  Backbone of FastAPI, enabling request and response validation.

- 🔒 **Data Safety**  
  Ensures only valid and expected data enters your API.

- 📥 **Automatic Request Parsing**  
  Parses incoming JSON into strongly typed Python objects automatically.

- 📤 **Response Modeling**  
  Defines and documents structured API responses using data models.

- 🧪 **Fewer Bugs**  
  Catches incorrect types and missing fields early.

- 📘 **Self-documenting APIs**  
  Generates OpenAPI schema docs automatically when used with frameworks like FastAPI.

---

## 🛠️ Step 1: Getting Started with Pydantic

Let’s explore Pydantic with examples before integrating it into a FastAPI app.

You can take the last step code as the base or **quickly set up a new project** using the following commands:

```bash
uv init fastdca_p1
cd fastdca_p1
uv venv
source .venv/bin/activate
uv add "fastapi[standard]"
```

## 📗 Step 2: Basic Pydantic Model

Let’s start by understanding how to define and use a simple Pydantic model.

Create a file named `pydantic_example_1.py`:

```python
from pydantic import BaseModel, ValidationError

# Define a simple model
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None  # Optional field with default None

# Valid data
user_data = {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 25}
user = User(**user_data)
print(user)  
print(user.model_dump())  

# Invalid data (will raise an error)
try:
    invalid_user = User(id="not_an_int", name="Bob", email="bob@example.com")
except ValidationError as e:
    print(e)
