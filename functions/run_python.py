import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    wd_abs_path = os.path.abspath(working_directory)
    if not abs_path.startswith(wd_abs_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try: 
        result = subprocess.run(["python3", abs_path], text=True, timeout=30, capture_output=True)
        if result.returncode != 0:
            return f'Process exited with code {result.returncode}'
        if len(result.stdout) == None:
            return "No output produced."
        if result.stderr:
            return f'STDERR: {result.stderr}'
        return f'STDOUT: {result.stdout}'
    except Exception as e:
        return f"Error: executing Python file: {e}"