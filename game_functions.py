def get_file_names():
    with open("file_names.txt", "r") as file:
        content = file.read()
    return content

