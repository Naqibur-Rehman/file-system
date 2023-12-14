import files

quit = False


def instructions():
    print("=============== In Memory File System ===================")
    print("This sytem support following commands")
    print(
        "1. mkdir directory_name \t ex- mkdir home, mkdir home/data \t creates folder"
    )
    print("2. cd path \t\t\t ex- cd home/data \t\t\t change directory")
    print(
        "3. ls path \t\t\t ex- ls home/data \t\t\t list the files and folders for the given path"
    )
    print("4. cat file_path \t\t ex- cat home/data.txt \t\t\t read the content of file")
    print("5. touch file_path \t\t ex- touch home/data.txt \t\t create empty file")
    print(
        "6. echo file_path content \t ex- echo home/data.txt soe text \t Write to a text file."
    )
    print(
        "7. mv src_path dest_path \t ex- mv home/data.txt /raw/data/ \t Move a file or directory to another location"
    )
    print(
        "8. cp src_path dest_path\t ex- cp home/data.txt /raw/new.text \t Copy a file or directory to another location."
    )
    print("9. rm path \t\t\t ex- rm home/data.txt \t\t\t Remove a file or directory.")
    print(
        "10. grep pattern file \t\t ex- touch hello home/data.txt \t\t Search for a pattern in file."
    )
    print("11. exit \t\t\t ex- exit \t\t\t\t To exit type exit")
    print("12. help \t\t\t ex- help \t\t\t\t To read instructions.")


instructions()

while not quit:
    userInput = input()
    command = userInput.split(" ")
    operation = command[0]
    # print(operation)

    if operation == "mkdir":
        files.mkdir(command)
    elif operation == "cd":
        files.cd(command)
    elif operation == "ls":
        files.ls(command)
    elif operation == "cat":
        files.cat(command)
    elif operation == "touch":
        files.touch(command)
    elif operation == "echo":
        files.echo(command)
    elif operation == "mv":
        files.mv(command)
    elif operation == "cp":
        files.cp(command)
    elif operation == "rm":
        files.rm(command)
    elif operation == "grep":
        files.grep(command)
    elif operation == "exit":
        quit = True
    elif operation == "help":
        instructions()
