"""Display all files in particular path"""
import os
from folder import folder

class files:

    def __init__(self):
        self.folders = folder()

    def show(self, path = '/media'):
        #lists all the files in of the given path

        if path:
            folders = self.folders.getdirs(search = path)
            files = []
            for x in folders:
                files.extend([f for f in os.listdir(x) if os.path.isfile(os.path.join(x, f))])

            return files

        else:
            return "invalid option"
