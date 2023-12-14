# In Memory File System

A filesystem that is stored in memory.

Memory filesystems are useful for caches, temporary data stores, unit testing, etc. Since all the data is in memory, they are very fast, but non-permanent.

## Requirements

To Run this project you need the following dependencies installed on your system.

- Python - If Python is not installed on your system you can download and install it from the official website of [Python](https://www.python.org/downloads/).
- PyFilesystem - Open cmd/shell and install PyFilesystem by running the following command.

```sh
pip install fs
```

- Now run the main.py file and enjoy 😎

## Documentation

Memory File System has the following functionalities:

1. `mkdir`: Create a new directory.
2. `cd`: Changes the current directory.
3. `ls`: List the contents of the current directory or a specified directory.
4. `grep`: Search for a specified pattern in a file.
5. `cat`: Display the contents of a file.
6. `touch`: Create a new empty file.
7. `echo`: Write text to a file.
8. `mv`: Move a file or directory to another location.
9. `cp`: Copy a file or directory to another location.
10. `rm`: Remove a file or directory.
11. `exit`: To exit from the program.
12. `help`: To see instructions.

| Sr. No. | Command                  | Example                            | Function                                                             |
| ------- | ------------------------ | --------------------------------   | -------------------------------------------------------------------- |
| 1.      | `mkdir directory_name`   | `mkdir home`, `mkdir home/data`    | Create a new directory.                                              |
| 2.      | `cd path`                | `cd home/data`                     | Changes the current directory.                                       |
| 3.      | `ls path`                | `ls home/data`                     | List the contents of the current directory or a specified directory. |
| 4.      | `cat file_path`          | `cat home/data.txt`                | Display the contents of a file.                                      |
| 5.      | `touch file_path`        | `touch home/data.txt`              | Create a new empty file.                                             |
| 6.      | `echo file_path content` | `echo home/data.txt soe text`      | Write a text to a file.                                              |
| 7.      | `mv src_path dest_path`  | `mv home/data.txt /raw/data/`      | Move a file or directory to another location.                        |
| 8.      | `cp src_path dest_path`  | `cp home/data.txt /raw/new.text`   | Copy a file or directory to another location.                        |
| 9.      | `rm path`                | `rm home/data.txt`                 | Remove a file or directory.                                          |
| 10.     | `grep pattern file`      | `touch hello home/data.txt`        | Search for a pattern in file.                                        |
| 11.     | `exit`                   | `exit`                             | To exit the program.                                                 |
| 12.     | `help`                   | `help`                             | To read instructions.                                                |
