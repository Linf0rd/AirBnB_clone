#!/usr/bin/python3
"""
Console Module
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the AirBnB clone project.
    """

    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State", "City",
                     "Amenity", "Place", "Review"]

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

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

    def do_create(self, arg):
        """
        Creates a new instance of a class, saves it (to the JSON file),
        and prints the ID.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and ID.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and ID
        (saves the change into the JSON file).
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of all instances
        based or not on the class name.
        """
        args = arg.split()
        all_objs = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in all_objs.values()])
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            class_objs = [
                    str(obj) for obj in all_objs.values()
                    if type(obj).__name__ == class_name
            ]
            print(class_objs)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and ID
        by adding or updating an attribute.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in all_objs:
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    attr_name = args[2]
                    attr_value = args[3]
                    obj = all_objs[key]
                    if hasattr(obj, attr_name):
                        attr_type = type(getattr(obj, attr_name))
                        setattr(obj, attr_name, attr_type(attr_value))
                        obj.save()
                    else:
                        print("** attribute doesn't exist **")
            else:
                print("** no instance found **")

    def default(self, line):
        """
        Override default method to handle <class name>.all(),
        <class name>.count(), <class name>.show(<id>),
        <class name>.destroy(<id>), <class name>.update(<id>,
        <attribute name>, <attribute value>), and
        <class name>.update(<id>, <dictionary representation>) commands.
        """
        if ".all()" in line:
            class_name = line.split(".")[0]
            if class_name in self.valid_classes:
                self.do_all(class_name)
            else:
                print("** class doesn't exist **")
        elif ".count()" in line:
            class_name = line.split(".")[0]
            if class_name in self.valid_classes:
                all_objs = storage.all()
                class_objs = [
                        obj for obj in all_objs.values()
                        if type(obj).__name__ == class_name
                ]
                print(len(class_objs))
            else:
                print("** class doesn't exist **")
        elif ".show(" in line:
            class_name = line.split(".")[0]
            if class_name in self.valid_classes:
                id_start = line.find("(") + 1
                id_end = line.find(")")
                instance_id = line[id_start:id_end].replace("\"", "")
                all_objs = storage.all()
                key = "{}.{}".format(class_name, instance_id)
                if key in all_objs:
                    print(all_objs[key])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif ".destroy(" in line:
            class_name = line.split(".")[0]
            if class_name in self.valid_classes:
                id_start = line.find("(") + 1
                id_end = line.find(")")
                instance_id = line[id_start:id_end].replace("\"", "")
                all_objs = storage.all()
                key = "{}.{}".format(class_name, instance_id)
                if key in all_objs:
                    del all_objs[key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif ".update(" in line:
            class_name = line.split(".")[0]
            if class_name in self.valid_classes:
                id_start = line.find("(") + 1
                id_end = line.find(",")
                instance_id = line[id_start:id_end].replace("\"", "").strip()
                dictionary_start = line.find(", {") + 1
                dictionary_end = line.find("})") + 1
                dictionary_str = line[dictionary_start:dictionary_end]
                dictionary = json.loads(dictionary_str)
                all_objs = storage.all()
                key = "{}.{}".format(class_name, instance_id)
                if key in all_objs:
                    obj = all_objs[key]
                    for attr_name, attr_value in dictionary.items():
                        if hasattr(obj, attr_name):
                            attr_type = type(getattr(obj, attr_name))
                            setattr(obj, attr_name, attr_type(attr_value))
                        else:
                            setattr(obj, attr_name, attr_value)
                    obj.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
