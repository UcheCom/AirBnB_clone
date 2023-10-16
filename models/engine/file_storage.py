#!/usr/bin/python3
""" Model creates a 'BaseModel' from another one
by using a dictionary representation
"""
import json
import os


class FileStorage():
    """ This serializes instances to a JSON file
    and deserializes JSON file to instances.
    Attribures:
        __file_path (str): Path to the JSON file
        __objects (dict): Stores all objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects. """
        return (FileStorage.__objects)

    def new(self, obj):
        """ Set in __objects obj with key <obj_class_name>.id """
        nw_obj = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(nw_obj, obj.id)] = obj

    def save(self):
        """ Serializes __object to JSON file in a file path
        """
        nw_dic = {}
        for key in FileStorage.__objects.keys():
            nw_dic[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as des_file:
            json.dump(nw_dic, des_file)

    def reload(self):
        """Deserializes the JSON file to __object
        if the file path exist
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        o_dic = {
                'BaseModel': BaseModel,
                'User': User,
                'Place': Place,
                'City': City,
                'State': State,
                'Amenity': Amenity,
                'Review': Review
        }

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path) as des_file:
                r_objs = json.load(des_file)

                for k, v in r_objs.items():
                    self.new(o_dic[v['__class__']](**v))
