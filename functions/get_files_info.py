import os

def get_files_info(working_directory, directory=None):
   abs_path = os.path.abspath(os.path.join(working_directory, directory))
   wd_abs_path = os.path.abspath(working_directory)
   if not abs_path.startswith(wd_abs_path):
      return print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
   if not os.path.isdir(abs_path):
      return print(f'Error: "{directory}" is not a directory')
   file_list = os.listdir(abs_path)
   output = []
   for item in file_list:
      item_path = os.path.join(abs_path, item)
      size = os.path.getsize(item_path)
      if os.path.isfile(item_path):
         output.append(f'- {item}: file_size={size} bytes, is_dir=False')
      if os.path.isdir(item_path):
         output.append(f'- {item}: file_size={size} bytes, is_dir=True')
   return print("\n".join(output))
