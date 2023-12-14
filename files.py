import fs
import re

mem_fs = fs.open_fs("mem://")
current_dir = mem_fs


mem_fs.makedir("data")
mem_fs.makedir("data/inside_data")
mem_fs.touch("hello.txt")
mem_fs.writetext("hello.txt", "hello, how are you world")


def mkdir(command):
    try:
        if len(command) == 1 or command[1] == "":
            print("Name of directory to be created is not provided by the user.")
        else:
            mem_fs.makedir(command[1])
            print(f"{command[1]} created successfully.")
    except Exception as err:
        print(err)


def changedir(path, mem_fs=mem_fs):
    current_dir = mem_fs
    if path == "/":
        current_dir = mem_fs

    components = path.split("/")

    for component in components:
        if component == "" or component == ".":
            continue
        elif component == "..":
            current_dir = current_dir.get_parent()
        else:
            current_dir = current_dir.opendir(component)
            mem_fs = fs.open_fs(current_dir, cwd=path)


def cd(command):
    try:
        if len(command) == 1 or command[1] == "":
            print("Path not provided")
        else:
            changedir(command[1])
    except Exception as err:
        print(err)


def ls(command):
    try:
        if len(command) == 1:
            print(mem_fs.listdir("."))
        else:
            print(mem_fs.listdir(command[1]))
    except Exception as err:
        print(err)


def cat(command):
    try:
        if len(command) == 1 or command[1] == "":
            print("Path not provided")
        else:
            ioStream = mem_fs.open(command[1])
            data = ioStream.read()
            print(data)
    except Exception as err:
        print(err)


def touch(command):
    try:
        if len(command) == 1 or command[1] == "":
            print("Path/File name not provided.")
        else:
            mem_fs.touch(command[1])
    except Exception as err:
        print(err)


def echo(command):
    try:
        if len(command) == 1 or command[1] == "":
            print("Path not provided.")
        else:
            content = ""
            for i in range(2, len(command)):
                content += command[i] + " "
            mem_fs.writetext(command[1], content)
    except Exception as err:
        print(err)


def mv(command):
    try:
        if len(command) == 1 or command[1] == "":
            print("Source and destination path not provided.")
        elif len(command) == 2 or command[2] == "":
            print("Destination not provided.")
        elif mem_fs.isfile(command[1]):
            mem_fs.move(command[1], command[2])
        elif mem_fs.isdir(command[1]):
            mem_fs.movedir(command[1], command[2], create=True)
    except Exception as err:
        print(err)


def cp(command):
    try:
        if len(command) == 1 or command[1] == "":
            print("Source and destination path not provided.")
        elif len(command) == 2 or command[2] == "":
            print("Destination not provided.")
        elif mem_fs.isfile(command[1]):
            mem_fs.copy(command[1], command[2], overwrite=True)
        elif mem_fs.isdir(command[1]):
            mem_fs.copydir(command[1], command[2], create=True)
    except Exception as err:
        print(err)


def rm(command):
    try:
        if len(command) == 1 or command[1] == "":
            print("Path not provided")
        else:
            type = mem_fs.gettype(command[1])
            if type == 1:
                mem_fs.removedir(command[1])
                print("Directory deleted successfully.")
            elif type == 2:
                mem_fs.remove(command[1])
                print("file deleted successfully.")
    except Exception as err:
        print(err)


def grep(command):
    try:
        if len(command) == 1 or command[1] == "":
            print("Pattern not provided")
        elif len(command) == 2 or command[2] == "":
            print("File path not provided")
        else:
            pattern = command[1]
            file = command[2]
            with mem_fs.open(file, "r") as f:
                for line in f:
                    if re.search(pattern, line):
                        print(f"Found: {line}")
                else:
                    print(f"{pattern} not found in file")
    except Exception as err:
        print(err)
