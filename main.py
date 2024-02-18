from file_operations import read_file, write_file
from user_input import get_file_name, get_file_content


def main():
    print("File Management System")

    file_name = get_file_name()

    print("Select operation:")
    print("1. Read File")
    print("2. Write to File")

    choice = input("Enter choice (1/2): ")

    if choice == '1':
        content = read_file(file_name)
        print(f"Content of '{file_name}':\n{content}")
    elif choice == '2':
        content = get_file_content()
        write_file(file_name, content)
    else:
        print("Invalid input. Please enter a valid choice.")


if __name__ == "__main__":
    main()
