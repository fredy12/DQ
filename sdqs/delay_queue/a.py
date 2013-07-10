import os.path
print os.path.dirname(__file__)
print os.path.join(os.path.dirname(__file__), 'templates').replace('\\', '/')
