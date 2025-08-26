from fastapi import FastAPI
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Session

app = FastAPI()

@app.get("/")
def root():
    return "Hello World"