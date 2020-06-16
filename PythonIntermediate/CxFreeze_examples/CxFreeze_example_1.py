# While sharing a python program for use , the recipient is going to need to have the same
# version of Python installed, along with all of the modules used.

#With Python 2.7, Py2exe is a great choice. For Python 3, cx_freeze may help
#cx_Freeze is a set of scripts and modules for freezing Python scripts into executables
#It is cross-platform and should work on any platform that Python itself works on

from cx_Freeze import setup, Executable

setup(name = "readURLLlib" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("resources/readURLLib.py")])

#Next Build the executable using: python CxFreeze_example_1.py build
