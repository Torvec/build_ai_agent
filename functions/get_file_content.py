import os
from google.genai import types

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    wd_abs_path = os.path.abspath(working_directory)
    if not abs_path.startswith(wd_abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_path, "r") as f:
            file_content_string = f.read()
        if len(file_content_string) > MAX_CHARS:
            return f'{file_content_string[:MAX_CHARS]}[...File "{file_path}" truncated at 10000 characters]'
        return file_content_string
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the file contents and returns it as a string, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file to read, relative to the working directory.",
            ),
        },
    ),
)