import os

default = []

# recursivly add all modules in the local directory to default with '.' separators in relation to this file
for root, dirs, files in os.walk(os.path.dirname(__file__)):
    for file in files:
        if file.endswith('.py') and file != '__init__.py':
            default.append('scales' + os.path.join(root, file).replace(os.path.dirname(__file__), '').replace('.py', '').replace(os.path.sep, '.'))
