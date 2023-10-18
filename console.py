#!/usr/bin/python3
"""A command interpreter for the AirBnB project"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """A class that inherits from cmd.Cmd
    Console command class.
    """

    prompt = "(hbnb) "
    o_dic = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }
    cmds = ['create', 'show', 'destroy', 'update', 'all,', 'count']

    def precmd(self, args):
        """ This Parses/tokenizes input and returns cmd with args"""
        if '.' in args and '(' in args and ')' in args:
            arg_list = args.split('.')
            _cmd = arg_list[1].split('(')
            _args = _cmd[1].split(')')
            if arg_list[0] in HBNBCommand.o_dic.keys() and \
               _cmd[0] in HBNBCommand.cmds:
                args = _cmd[0] + ' ' + arg_list[0] + ' ' + _args[0]
            elif arg_list[0] in HBNBCommand.o_dic.keys() and \
                    _cmd[0] == 'counter':
                args = 'counter' + ' ' + arg_list[0]
        return args

    def do_create(self, arg):
        """Create command creates new instance,
        saves it to JSON file & prints the id.
        Usage: create <class>
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.o_dic.keys():
            print("** class doesn't exist **")
        else:
            b_mod = HBNBCommand.o_dic[arg]()
            print(b_mod.id)
            b_mod.save()

    def do_show(self, args):
        """Print the string representation of an instance.
        Usage: show <class_name> <id>
        """
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split(' ')
        cl_name = arg_list[0]

        if cl_name not in HBNBCommand.o_dic.keys():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for obj in all_objs.values():
                n_class = obj.__class__.__name__
                if n_class == cl_name and obj.id == arg_list[1].strip('"'):
                    print(obj)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split(' ')
        cl_name = arg_list[0]

        if cl_name not in HBNBCommand.o_dic.keys():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for (k, v) in all_objs.items():
                n_class = v.__class__.__name__
                obj_id = v.id
                if n_class == cl_name and obj_id == arg_list[1].strip('"'):
                    del v
                    del storage._FileStorage__objects[k]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based
        or not on the class name
        Usage: all or all <class_name>
        """
        all_objs = storage.all()
        list_str = []

        if not args:
            for (k, obj) in all_objs.items():
                list_str.append(obj.__str__())
            print(list_str)
        else:
            arg_list = args.split(' ')
            cl_name = args[0]
            if cl_name not in HBNBCommand.o_dic.keys():
                print("** class doesn't exist **")
            else:
                for (k, obj) in all_objs.items():
                    n_class = obj.__class__.__name__
                    if n_class == cl_name:
                        list_str.append(obj.__str__())
                print(list_str)

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        Usage: update <class_name> <obj_id> <attribute_name>
        <attribute_value>)
        """

        if not args:
            print("** class name missing **")
            return
        argv = ""
        for ab in args.split(','):
            argv += ab
        arg_list = shlex.split(argv)
        cl_name = args[0]
        if cl_name not in HBNBCommand.o_dic.keys():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for (k, obj) in all_objs.items():
                cls_name = obj.__class__.__name__
                if cls_name == cl_name and obj_id == args[1].strip('"'):
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        if isinstance(args[2], dict):
                            for (key, val) in args[2].items():
                                setattr(obj, key, val)
                                obj.save()
                        else:
                            print("** value missing **")
                    else:
                        setattr(obj, args[2], args[3])
                        obj.save()
                    return
            print("** no instance found **")

    def do_count(self, args):
        """ Counts and prints the number of instances of a class
        Usage: count <class_name>
        """
        all_objs = storage.all()

        counter = 0
        for k, obj in all_objs.items():
            cls_name = obj.__class__.__name__
            if cls_name == args:
                counter += 1
        print(counter)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
