#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
    __file_path (str): The name of the file to save objects to.
    __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects
    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        obj_clname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_clname, obj.id)] = obj
        
    def save(self):
        """Serialize __objects to the JSON file __file_path"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(objdict , json_file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects (if it exists)."""
        try:
            with open(FileStorage.__file_path, 'r') as json_file:
                objdict = json.load(json_file)
                for obj in objdict.values():
                    clname = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(clname)(**obj))
        except FileNotFoundError:
            return 


