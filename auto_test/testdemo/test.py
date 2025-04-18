import os,inspect

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_File_Name = os.path.splitext(os.path.relpath(inspect.stack()[-1].filename, project_root))[0].replace(os.sep, '_')

print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(project_root)
print(os.path.relpath(inspect.stack()[-1].filename, project_root))
print(os.path.splitext(os.path.relpath(inspect.stack()[-1].filename, project_root))[0])