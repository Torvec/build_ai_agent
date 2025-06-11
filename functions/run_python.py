import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    wd_abs_path = os.path.abspath(working_directory)
    if not abs_path.startswith(wd_abs_path):
        return print(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    if not os.path.exists(abs_path):
        return print(f'Error: File "{file_path}" not found.')
    if not file_path.endswith(".py"):
        return print(f'Error: "{file_path}" is not a Python file.')
    result = subprocess.run(["python3", abs_path], text=True, timeout=30, capture_output=True)
    try: 
        if result.returncode != 0:
            return print(f'Process exited with code {result.returncode}')
        if len(result.stdout) == None:
            return print("No output produced.")
        if result.stderr:
            return print(f'STDERR: {result.stderr}')
        return print(result.stdout)
    except Exception as e:
        return print(f"Error: executing Python file: {e}")