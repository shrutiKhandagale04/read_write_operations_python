# file_operations.py

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"File '{file_name}' not found."

def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"Content written to '{file_name}'.")
