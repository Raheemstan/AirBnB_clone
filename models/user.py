#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel

class User(BaseModel):
    """This is the class for user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""