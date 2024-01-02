import os

def mkch(path):
    try:
        os.mkdir(path)
    except:
        pass
    os.chdir(path)