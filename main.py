from fastapi import FastAPI
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Session

# Database URL and engine creation for SQLite
DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal class instance will be the database session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for declarative class definitions
Base = declarative_base()

# Database model for projects
class Project(Base):
    """Database model for projects"""
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, index=True)
    project_description = Column(String)

    # A project can have many students
    students = relationship("Student", back_populates="project")


# Database model for students
class Student(Base):
    """Database model for students"""
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    linkedin_profile = Column(String, nullable=True)
    about_you = Column(String, nullable=True)
    specialisation = Column(String, nullable=True)
    cgpa = Column(Float, nullable=True)
    favourite_language = Column(String, nullable=True)
    favourite_framework = Column(String, nullable=True)
    is_leader = Column(Boolean, default=False)

    # Each student may belong to a project
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=True)

    # Relationship back to project
    project = relationship("Project", back_populates="students")

# Pydantic schema for project base data validation
class ProjectBase(BaseModel):
    project_name: str
    project_description: str

# Pydantic schema for project including ID and ORM mode
class ProjectSchema(ProjectBase):
    id: int
    class Config:
        orm_mode = True


# Student schemas

# Pydantic schema for student base data validation
class StudentBase(BaseModel):
    name: str
    email: str
    linkedin_profile: Optional[str] = None
    about_you: Optional[str] = None
    specialisation: Optional[str] = None
    cgpa: Optional[float] = None
    favourite_language: Optional[str] = None
    favourite_framework: Optional[str] = None
    is_leader: bool = False
    project_id: Optional[int] = None

# Pydantic schema for student including ID and ORM mode
class StudentSchema(StudentBase):
    id: int
    class Config:
        orm_mode = True

# Create FastAPI app instance
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint returning a simple greeting
# http://localhost:8000/
@app.get("/")
def root():
    return "Hello World"

# Endpoint to create a new project
# http://localhost:8000/projects
@app.post("/projects/", response_model=ProjectSchema, status_code=201)
def create_project(project: ProjectBase, db: Session = Depends(get_db)):
    new_project = Project(**project.model_dump())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project