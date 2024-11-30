# write a python program to print the contents of a directory using the os module online for the function which does that.
import os

def print_directory_contents(directory):
    try:
        # List all files and directories in the specified directory
        contents = os.listdir(directory)
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")

# Specify the directory you want to list
directory_path = '.'  # Current directory
print_directory_contents('/home/vijay/Desktop')
