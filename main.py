from fastapi import FastAPI
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Session

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

class Project(Base):
    """Database model for projects"""
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, index=True)
    project_description = Column(String)

    # A project can have many students
    students = relationship("Student", back_populates="project")


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


app = FastAPI()

@app.get("/")
def root():
    return "Hello World"