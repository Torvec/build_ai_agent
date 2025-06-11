import os

def write_file(working_directory, file_path, content):
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    wd_abs_path = os.path.abspath(working_directory)
    if not abs_path.startswith(wd_abs_path):
        return print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    with open(abs_path, "w") as f:
        f.write(content)
    return print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
