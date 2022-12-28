#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 12:34:09 2022

@author: nikhil
"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'mesaage': 'Hello, nikhil'}

@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome to Tech With Nick youtube channel': f'{name}'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port=8000)
    
#uvicorn main:app --reload    
