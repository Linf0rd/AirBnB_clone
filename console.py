#!/usr/bin/python3
"""
Console Module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the AirBnB clone project.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when End-of-File (EOF) is reached.
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
