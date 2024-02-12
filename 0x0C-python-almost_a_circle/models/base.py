#!/usr/bin/python3
""" class named Base """
import json


class Base():
    """ the base of all other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializing the id and set it to value """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string rep
        of list_dictionaries
        list_dictionaries is a list of dictionaries
        if list_dictionaries is empy or None return []
        """
        
        if not list_dictionaries:
            return "[]"

        json_str = json.dumps(list_dictionaries)

        return json_str

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes json string representation of list_objs
        to a file, overwrite if it already exists
        @list_objs: list of instances who inherit of Base
        """

        if list_objs is None:
            json_obj_str = "[]"

        json_obj_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding='utf-8') as f:
            f.write(json_obj_str)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation
        @json_string: is a string representing list of dict
        """
        if not json_string:
            return "[]"

        from_json = json.loads(json_string)
        return from_json

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set
        @dictionary: can be thought of as double pointer to dict
        """

        # creating dummy instance
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 2, 0, 0, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(2, 0, 0, 1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances
        filename must be <Class name>.json
        if file does not exist, return empty list
        """
        filename = cls.__name__ + ".json"
        instances = []

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                cont = f.read()

            from_json_file = cls.from_json_string(cont)
            for data in from_json_file:
                instances.append(cls.create(**data))
        except FileNotFoundError:
            pass
        return instances
