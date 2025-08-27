# FastAPI Student Project Management API

This repository provides a simple FastAPI-based API for managing student and project information, using SQLAlchemy for database operations and Pydantic for data validation.

## Features

- **Projects**: Create and manage project records.
- **Students**: Store student details, including specialisation, CGPA, and project assignment.
- **Relational Database**: Students are linked to projects via foreign key relationships.
- **RESTful Endpoints**: Easily interact with the API using HTTP requests.

## Technologies Used

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite (local database)

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi sqlalchemy pydantic uvicorn
   ```

3. **Initialize the database**
   The database (`app.db`) will be created automatically when you run the app for the first time.

### Running the API

Start the server using Uvicorn:
```bash
uvicorn <your_python_file>:app --reload
```
Replace `<your_python_file>` with the filename containing your code.

### API Endpoints

- `GET /`  
  Returns a simple "Hello World" message.

- `POST /projects/`  
  Create a new project.  
  **Request Body:**  
  ```json
  {
    "project_name": "Project Title",
    "project_description": "Description here"
  }
  ```

  **Response:**  
  Returns the created project object.

## Project Structure

- **models**: SQLAlchemy models for `Project` and `Student`.
- **schemas**: Pydantic schemas for input/output validation.
- **main app**: FastAPI endpoints for project management.

## Notes

- The database uses SQLite for easy local setup.
- Extend the API by adding more endpoints (e.g., for students, updating projects, etc.).
- Use the `/docs` endpoint for interactive API documentation (Swagger UI).

## License

MIT License