import sys
import os

def InitSystemPath():
    FolderPathPython = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(FolderPathPython+ '\\Shoulder_env')
    sys.path.append(FolderPathPython+ '\\Shoulder_env\\lib')
    sys.path.append(FolderPathPython+ '\\Shoulder_env\\lib\\site-packages')
    #print ( "test " + sys.path)
