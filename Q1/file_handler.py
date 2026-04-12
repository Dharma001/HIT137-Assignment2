def read_file(filename):
    """
    Reads the content of a file and returns it as a string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def write_file(filename, content):
    """
    Writes the given content to a file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)