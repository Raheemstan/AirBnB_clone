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
        """Show command implementation."""
        # Implement logic to show details of an instance
        pass

    def do_destroy(self, arg):
        """Destroy command implementation."""
        # Implement logic to delete an instance based on arg
        pass

    def do_all(self, arg):
        """All command implementation."""
        # Implement logic to show all instances
        pass

    def do_update(self, arg):
        """Update command implementation."""
        # Implement logic to update an instance
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
