# Algorithm:

# We use a dictionary to represent the directory, where the keys are the file names and the values are empty strings (representing the file contents).
# The create_file function adds a new file to the directory.
# The delete_file function removes a file from the directory if it exists.
# The list_files function prints all the files in the directory.

directory = {}

def create_file(name):
    directory[name] = ""

def delete_file(name):
    if name in directory:
        del directory[name]
    else:
        print("File not found")

def list_files():
    for file in directory:
        print(file)

create_file("file1")
create_file("file2")
create_file("file3")
list_files()
delete_file("file2")
list_files()

# Algorithm:

# We use a dictionary to represent the root directory, where the keys are the subdirectory names and the values are dictionaries representing the subdirectories.
# The create_directory function adds a new subdirectory to the root directory.
# The create_file function adds a new file to a subdirectory.
# The delete_file function removes a file from a subdirectory if it exists.
# The list_files function prints all the files in a subdirectory.
root = {}

def create_directory(name):
    if name not in root:
        root[name] = {}

def create_file(directory, name):
    if directory in root:
        root[directory][name] = ""

def delete_file(directory, name):
    if directory in root and name in root[directory]:
        del root[directory][name]
    else:
        print("File not found")

def list_files(directory):
    if directory in root:
        for file in root[directory]:
            print(file)
    else:
        print("Directory not found")

create_directory("dir1")
create_directory("dir2")
create_file("dir1", "file1")
create_file("dir1", "file2")
create_file("dir2", "file3")
list_files("dir1")
delete_file("dir1", "file2")
list_files("dir1")


# Algorithm:

# We use a dictionary to represent the file system, where the keys are the directory names and the values are dictionaries representing the subdirectories and files.
# The create_directory function adds a new subdirectory to a parent directory.
# The create_file function adds a new file to a directory.
# The delete_file function removes a file from a directory if it exists.
# The list_files function prints all the files and subdirectories in a directory.

root = {}
def create_directory(parent, name):
    if parent in root:
        if name not in root[parent]:
            root[parent][name] = {}
    else:
        print("Parent directory not found")

def create_file(parent, name):
    if parent in root:
        root[parent][name] = ""

def delete_file(parent, name):
    if parent in root and name in root[parent]:
        if isinstance(root[parent][name], dict):
            print("Cannot delete a directory")
        else:
            del root[parent][name]
    else:
        print("File not found")

def list_files(parent):
    if parent in root:
        for file in root[parent]:
            if isinstance(root[parent][file], dict):
                print(file + "/")
            else:
                print(file)
    else:
        print("Directory not found")

create_directory("", "dir1")
create_directory("dir1", "dir2")
create_file("dir1", "file1")
create_file("dir2", "file2")
list_files("dir1")
delete_file("dir1", "file1")
list_files("dir1")


# Algorithm:

# We use a dictionary to represent the graph, where the keys are the directory names and the values are dictionaries representing the subdirectories and files.
# The create_directory function adds a new directory to the graph.
# The create_file function adds a new file to a directory.
# The delete_file function removes a file from a directory if it exists.
# The list_files function prints all the files in a directory.
# The create_link function creates a link between two directories.

graph = {}

def create_directory(name):
    if name not in graph:
        graph[name] = {"subdirs": {}, "files": {}}

def create_file(directory, name):
    if directory in graph:
        graph[directory]["files"][name] = ""

def delete_file(directory, name):
    if directory in graph and name in graph[directory]["files"]:
        del graph[directory]["files"][name]
    else:
        print("File not found")

def list_files(directory):
    if directory in graph:
        for file in graph[directory]["files"]:
            print(file)
    else:
        print("Directory not found")

def create_link(src, dst):
    if src in graph and dst in graph:
        graph[src]["subdirs"][dst] = ""

create_directory("dir1")
create_directory("dir2")
create_file("dir1", "file1")
create_file("dir2", "file2")
create_link("dir1", "dir2")
list_files("dir1")
delete_file("dir1", "file1")
list_files("dir1")

