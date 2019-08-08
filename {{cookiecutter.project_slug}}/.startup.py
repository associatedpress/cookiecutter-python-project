import os
import re
project_name = f"{{ cookiecutter.project_slug }}"
cwd = os.getcwd()
at_root_check = re.compile(r'.+' + project_name + '$')
if at_root_check.search(cwd):
    pass
else:
    root_path_search = re.compile(r'.+' + project_name)
    root_path = root_path_search.search(cwd).group()
    os.chdir(root_path)
    print(f"Working directory for ipython set to {root_path}")
