#!/usr/bin/python3
""" __init__ method models package """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
