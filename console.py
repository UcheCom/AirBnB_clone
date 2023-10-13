#!/usr/bin/python3
"""A command interpreter for the AirBnB project"""

import cmd

class HBNBCommand(cmd.Cmd):
    """A class that inherits from cmd.Cmd"""

    prompt = "(hbnb) "

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
