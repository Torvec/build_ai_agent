import os

def get_file_content(working_directory, file_path):
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    wd_abs_path = os.path.abspath(working_directory)
    if not abs_path.startswith(wd_abs_path):
        return print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    if not os.path.isfile(abs_path):
        return print(f'Error: File not found or is not a regular file: "{file_path}"')
    MAX_CHARS = 10000
    with open(abs_path, "r") as f:
        file_content_string = f.read()
    if len(file_content_string) > MAX_CHARS:
        return print(f'{file_content_string[:MAX_CHARS]}[...File "{file_path}" truncated at 10000 characters]')
    return print(file_content_string)