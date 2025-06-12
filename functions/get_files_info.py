import os
from google.genai import types

def get_files_info(working_directory, directory=None):
   abs_path = os.path.abspath(os.path.join(working_directory, directory))
   wd_abs_path = os.path.abspath(working_directory)
   if not abs_path.startswith(wd_abs_path):
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
   if not os.path.isdir(abs_path):
      return f'Error: "{directory}" is not a directory'
   try:
      file_list = os.listdir(abs_path)
      output = []
      for item in file_list:
         item_path = os.path.join(abs_path, item)
         size = os.path.getsize(item_path)
         if os.path.isfile(item_path):
            output.append(f'- {item}: file_size={size} bytes, is_dir=False')
         if os.path.isdir(item_path):
            output.append(f'- {item}: file_size={size} bytes, is_dir=True')
      return "\n".join(output)
   except Exception as e:
      return f"Error listing files: {e}"

schema_get_files_info = types.FunctionDeclaration(
   name="get_files_info",
   description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
   parameters=types.Schema(
      type=types.Type.OBJECT,
      properties={
            "directory": types.Schema(
               type=types.Type.STRING,
               description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
      },
   ),
)