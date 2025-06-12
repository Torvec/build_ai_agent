import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    wd_abs_path = os.path.abspath(working_directory)
    if not abs_path.startswith(wd_abs_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_path):
        try:
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        except Exception as e:
            return f'Error: creating directory {e}'
    if os.path.exists(abs_path) and os.path.isdir(abs_path):
        return f'Error: "{file_path}" is a directory, not a file'
    try: 
        with open(abs_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: writing to file: {e}'

schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Writes to a given file using the content provided, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file path of the file to write to, relative to the working directory.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The content to be written within the given file.",
                ),
            },
        ),
    )