# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn the fundamentals of building RESTful APIs using the FastAPI framework in Python. You will create a simple API for managing a collection of tasks, allowing you to practice creating, reading, updating, and deleting data through HTTP endpoints.

## 📝 Tasks

### 🛠️	Set Up FastAPI Project

#### Description
Install FastAPI and create a basic FastAPI application structure. This task focuses on getting your development environment ready and understanding the basics of FastAPI.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn using pip
- Create a main.py file with a basic FastAPI app instance
- Include a root endpoint (GET /) that returns a welcome message in JSON format
- Run the server and verify it works by visiting http://localhost:8000 in your browser

### 🛠️	Implement CRUD Endpoints

#### Description
Add endpoints for Create, Read, Update, and Delete operations on a simple task management system. This will help you understand how to handle different HTTP methods and data models.

#### Requirements
Completed program should:

- Define a Pydantic model for a Task with fields like id, title, description, and completed status
- Implement GET /tasks to retrieve all tasks
- Implement POST /tasks to add a new task
- Implement PUT /tasks/{task_id} to update an existing task
- Implement DELETE /tasks/{task_id} to delete a task
- Use an in-memory list to store tasks (no database required)
- Include proper error handling for non-existent tasks</content>
<parameter name="filePath">/workspaces/skills-customize-your-github-copilot-experience/assignments/rest-apis-fastapi/README.md