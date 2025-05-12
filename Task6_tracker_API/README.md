# 📝 Task Tracker API

Welcome to the **Task Tracker API**, a lightweight backend solution built with **FastAPI** and **Pydantic**.

This API helps you manage users and their assigned tasks with clean, simple endpoints for creating, retrieving, and updating records.

---

## 📘 Project Summary

### 🔹 1. Data Models

- **UserCreate**  
  - For registering a new user  
  - Requires:
    - `user_name` (between 3 to 20 characters)
    - `email` (must end in `.com`)

- **UserRead**  
  - Returned when retrieving user info  
  - Includes:
    - `user_id`
    - `user_name`
    - `email`

- **TaskCreate**  
  - Used to add a new task  
  - Requires:
    - `title` (mandatory)
    - `description` (optional)
    - `due_date` (must be today or later)
    - `user_id` (assigns the task to a user)
    - `status` (must be a valid status)

- **TaskRead**  
  - Inherits from TaskCreate  
  - Adds:
    - `id`
    - `created_at` timestamp

- **StatusUpdateModel**  
  - For modifying only the `status` of an existing task

---

### 🔹 2. In-Memory Storage

- `USERS`: Stores all users as key-value pairs using `user_id`
- `TASKS`: Stores all tasks with `task_id` as the key
- `ALLOWED_STATUSES`: Permitted task states are:
  - `pending`
  - `in_progress`
  - `completed`

---

### 🔹 3. Endpoints


| HTTP Method | Route                        | Description                              |
|-------------|------------------------------|------------------------------------------|
| GET         | `/`                          | Returns a welcome message                |
| POST        | `/users/`                    | Register a new user                      |
| GET         | `/users/{user_id}`           | Retrieve user details by ID              |
| POST        | `/tasks/`                    | Add a new task                           |
| GET         | `/tasks/{task_id}`           | Fetch a task using its ID                |
| PUT         | `/tasks/{task_id}`           | Update the status of a task              |
| GET         | `/users/{user_id}/tasks`     | List all tasks assigned to a user        |


# 🔄 Step-by-Step API Walkthrough (With Images)

## ℹ️ About This Section
This section visually walks you through how to use the Task Tracker API — from viewing the welcome message to creating users, managing tasks, and tracking their statuses. Each step includes reference images from Swagger UI to simplify your experience.

    
