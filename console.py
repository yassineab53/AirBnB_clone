#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd 
import json
import os

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass
    
    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True 
    
    def do_EOF(self, line):
        """Quit command to exit the program
        """
        return True 
    
    
    #aliasing
    #do_EOF = do_quit

if __name__ == "__main__":
    HBNBCommand().cmdloop()