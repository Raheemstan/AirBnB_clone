#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF (Ctrl+D) is reached"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass
    
    def do_create(self, arg):
        """Create command implementation."""
        # Implement logic to create an instance based on arg
        pass

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instances = storage.all()
            key = args[0] + '.' + args[1]
            if key not in instances:
                print("** no instance found **")
                return
            print(instances[key])
        except IndexError:
            pass
    
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instances = storage.all()
            key = args[0] + '.' + args[1]
            if key not in instances:
                print("** no instance found **")
                return
            del instances[key]
            storage.save()
        except IndexError:
            pass

    def do_all(self, arg):
        """Prints all string representation of all instances based on the class name."""
        if not arg:
            print("** class name missing **")
            return
        try:
            instances = storage.all()
            class_name = arg.split()[0]
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in instances if type(obj).__name__ == class_name])
        except IndexError:
            pass


    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instances = storage.all()
            key = args[0] + '.' + args[1]
            if key not in instances:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(instances[key], args[2], args[3])
            storage.save()
        except IndexError:
            pass


    def do_count(self, arg):
        """Counts instances of a class."""
        if not arg:
            print("** class name missing **")
            return
        try:
            count = 0
            instances = storage.all()
            class_name = arg.split()[0]
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            for obj in instances:
                if type(obj).__name__ == class_name:
                    count += 1
            print(count)
        except IndexError:
            pass

    def do_update_dict(self, arg):
        """Updates an instance based on the class name and id with a dictionary."""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instances = storage.all()
            key = args[0] + '.' + args[1]
            if key not in instances:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** dictionary missing **")
                return
            try:
                dict_str = args[2].replace("'", '"')
                new_dict = json.loads(dict_str)
            except ValueError:
                print("** invalid dictionary **")
                return
            for k, v in new_dict.items():
                setattr(instances[key], k, v)
            storage.save()
        except IndexError:
            pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
