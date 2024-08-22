# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:58:20 2024

@author: 2632
"""

from flask import Flask
from app_blueprint import app_blueprint

app= Flask(__name__)

app.register_blueprint(app_blueprint)