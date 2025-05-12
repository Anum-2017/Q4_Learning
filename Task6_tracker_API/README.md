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

---

# 🛠️ API Walkthrough: A Step-by-Step Guide (With Visuals)

## ℹ️ About This Section
This section visually walks you through how to use the Task Tracker API — from viewing the welcome message to creating users, managing tasks, and tracking their statuses. Each step includes reference images from Swagger UI to simplify your experience.

## 🔹Step 0: View the Welcome Message
 - Navigate to the root `http://127.0.0.1:8000/` GET endpoint
 - You will receive a welcome message confirming that the API is running:

#### 📝 Welcome Message

<img width="586" alt="1" src="https://github.com/user-attachments/assets/615d909d-d9b9-44ff-b26d-99a7388cdda9" />


## 🔹 Step 1: Access Swagger UI
 - Open the Swagger UI at `http://127.0.0.1:8000/docs`.
 - You can interact with the API documentation here to perform all tasks.

<img width="959" alt="2" src="https://github.com/user-attachments/assets/c9b47c2b-3c0b-46f4-b840-be172ba73489" />


## 🔹 Step 2: Create a User
 - Navigate to `/users/ POST` endpoint in Swagger UI (/docs)
 - Provide user_name and email
 - A new user_id will be generated

#### CreateUser

<img width="527" alt="3" src="https://github.com/user-attachments/assets/6a189d2e-bac8-4106-bce2-d1b1dbaa370f" />

#### Response_CreateUser

<img width="526" alt="4" src="https://github.com/user-attachments/assets/c670cdf3-e9a1-4df4-861c-731c337b6baa" />


## 🔹 Step 3: Get the Created User
 - Navigate to `/users/{user_id}` GET endpoint.
 - Enter the same user_id.
 - You will see the user_name and email returned.

#### GetUser

<img width="530" alt="5" src="https://github.com/user-attachments/assets/c90f61ba-6b8e-4217-b561-073cf3ce2856" />


## 🔹 Step 4: Create a Task
 - Head over to the `/tasks/ POST` endpoint using the Swagger UI.
 - Enter the following details to create a task:
     - title: The name of the task
     - description (optional): What the task is about
     - due_date: When the task should be completed (today or later)
     - user_id: The ID of the user the task belongs to
     - status: Current state of the task (e.g., pending)
 - Once submitted, a new task_id will be automatically generated for you.

#### Task_Creation

<img width="529" alt="6" src="https://github.com/user-attachments/assets/7a671b80-38f1-4199-b7d6-1f75e3573c5d" />

#### Response_Task_Creation

<img width="526" alt="7" src="https://github.com/user-attachments/assets/cede6d9a-f7be-43a0-9eef-956ca5b4a28e" />


## 🔹 Step 5: Get the Created Task
 - Navigate to `/tasks/{task_id}` GET endpoint.
 - Enter the task_id.
 - Task details will be displayed.

#### Get_Task

<img width="536" alt="8" src="https://github.com/user-attachments/assets/d60ba4ab-a03b-42d6-aa0d-5ca14db61856" />


## 🔹 Step 6: Update Task Status
 - Navigate to the `/tasks/{task_id}` PUT endpoint.
 - Input the specific task_id of the task you want to update.
 - Change the status field to reflect the current progress (e.g., from `in_progress` to `completed`).

#### Update_Task_Status

<img width="536" alt="9" src="https://github.com/user-attachments/assets/8b12875b-8f52-44f6-8ba4-9ed618203520" />

#### Response_Update_Task_Status

<img width="529" alt="10" src="https://github.com/user-attachments/assets/a1a43d70-1cba-411e-9885-1fbec46cd453" />


## 🔹 Step 7: Confirm Task Update
 - Navigate to `/tasks/{task_id}` GET endpoint again.
 - The updated status will be shown.

#### After_Updating_Task_Get

<img width="535" alt="11" src="https://github.com/user-attachments/assets/649a1549-0bfe-4b43-b007-6554e7221bac" />


## 🔹 Step 8: Get All Tasks for a User
 - Navigate to `/users/{user_id}/tasks` GET endpoint.
 - Enter the user_id.
 - All linked tasks will be shown.

#### Getting_User_Task

<img width="533" alt="12" src="https://github.com/user-attachments/assets/2cd387c1-40eb-4e1c-93a2-738c96b55d2b" />

---

##  🎯 Conclusion

 With the Task Tracker API, you now have a simple and efficient way to:

- 🧑‍💼 Manage Users – Easily create and retrieve user profiles.
- 📋 Create and Track Tasks – Link tasks to users, assign due dates, and monitor their statuses.
- 🔄 Update Progress – Change task statuses dynamically as progress is made.
- 📋 Retrieve Linked Data – View all tasks associated with specific users in one place.

All this can be done through the intuitive Swagger UI at http://127.0.0.1:8000/docs, making interaction smooth and beginner-friendly.

🎯 Whether you're building a personal to-do app or a small team project manager, this API is your foundation for structured task management.

## *Happy Tracking!* 🎯







