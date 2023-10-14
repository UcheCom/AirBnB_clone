#!/usr/bin/python3
"""A command interpreter for the AirBnB project"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):
    """A class that inherits from cmd.Cmd
    Console command class.
    """

    prompt = "(hbnb) "
    o_dic = {
        'BaseModel': BaseModel,
        'User': User,
    }
    cmds = ['create']
    
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
