import os
import sys
import shutil

class Destroyer:
    def destroyConfig():
        mydir= 'config'
        try:
            shutil.rmtree(mydir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
