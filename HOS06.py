from pathlib import Path

def read_or_create_file(file_path):
    """Reads the file if it exists; otherwise creates a new one."""
    try:
        contents = file_path.read_text()
        print("File found. Contents:")
        print(contents)
    except FileNotFoundError:
        print(f"File not found at {file_path}. Creating a new empty file.")
        file_path.touch()


def read_file_line_by_line(file_path):
    """Reads the file line by line and prints each line with a line number."""
    try:
        lines = file_path.read_text().splitlines()
        for line_number, line_content in enumerate(lines, start=1):
            print(f"{line_number}: {line_content}")
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")


def rename_file(current_path, new_path):
    """Renames a file and handles missing files or unexpected errors."""
    try:
        current_path.rename(new_path)
        print(f"File renamed to {new_path}")
    except FileNotFoundError:
        print(f"The file {current_path} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def delete_file(file_path):
    """Deletes the file if it exists; handles missing files and unexpected errors."""
    try:
        file_path.unlink()
        print(f"File {file_path} has been deleted.")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    file_path = Path("example.txt")
    read_or_create_file(file_path)

    print("\nOriginal file content:")
    read_file_line_by_line(file_path)

    new_file_path = Path("renamed_example.txt")
    rename_file(file_path, new_file_path)

    print("\nRenamed file content:")
    read_file_line_by_line(new_file_path)

    choice = input(f"\nDo you want to delete the file {new_file_path}? (y/n) ")
    if choice.lower() == "y":
        delete_file(new_file_path)

if __name__ == "__main__":
    main()


    