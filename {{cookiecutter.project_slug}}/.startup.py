import os
## This is the project directory name to set as root
project_name = f"{{ cookiecutter.project_slug }}"
## This is the current directory
cwd = os.getcwd()
## This is the basename of the current directory path
basename = os.path.basename(cwd)
## If we get all the way to the root of the file system,
## We'll use this to not change the directory
project_root_not_found = False

## While the basename does not equal the project name
## Use the split method to get the tail and head of the cwd
## The new cwd becomes the tail and we test it again
## If the head is ever an empty string, we found nothing, and
## do not change the directory.
while basename != project_name:
    if os.path.split(cwd)[1] == '':
        basename = project_name
        project_root_not_found = True
    else:
        cwd = os.path.split(cwd)[0]
        basename = os.path.basename(cwd)

if project_root_not_found:
    print("Couldn't find project root. Current directory not changed to project root.")
else:
    os.chdir(cwd)