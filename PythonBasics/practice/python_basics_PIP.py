#pip is the standard package manager for Python.
#- use pip to install additional packages that are not available in the Python standard library

#Documentation: https://pip.pypa.io/en/stable/

#Working with pip
import pip

#------------------ How to install pip------------------
#pip comes pre-installed on the Python versions 3.4 or older.
# We can check if pip is installed by using the following command in the console:

print(pip.__version__)

#Command Line: pip --version

#------------------Using pip---------------------------
#After its installation, a pip command is added which can be used with the command prompt.

#--------------Installing Packages with pip------------------
#Apart from the standard Python library, the Python community contributes to an extensive
# number of packages tailored for various development frameworks, tools, and libraries.

#Basic Package Installation: install command
#Example: install requests, a popular HTTP library for Python.
#Command Line:pip install requests

#Specifying Package Version:When pip install is used in its minimal form,
# pip downloads the most recent version of the package.
#Command Line: pip install requests==2.21.0

#-------------Listing Installed Packages with pip------------------
# list command : used to list all the available packages in the current Python environment.
#Command Line:pip list

#-------------- Package Information with pip show--------------------
#pip show: command displays information about one or more installed packages.
#Command Line:pip show requests
#Notes:
#- Requires column shows which dependencies the requests library requires.
#- Required-by column shows the packages that require requests.

#----------Uninstalling a Package with pip----------------------
#We can uninstall a package by using pip with the pip uninstall command.
#Command Line: pip uninstall requests

#----------Using Requirement Files---------------------
#A file containing all the package names can also be used to install Python packages in batches.
#Example:Suppose we have a file requirements.txt which has the following entries.
# We can install all these packages and their dependencies by using a single command in pip.
# Command Line: pip install -r requirements.txt
# Note:  additional argument -r specifies pip that we are passing a requirements file rather than a package name.

#To List the packages that don't come preinstalled will Python are listed using the freeze command.
# Command Line:pip freeze
#Note:
# - The pip freeze command displays the packages and their version in the format of the requirements file.
# - This output can be redirected to create a requirements file using the following command:
# Command Line: pip freeze > requirements.txt

#Note :
# - A new requirements.txt file is created in the working directory.
# - It can later be used in other Python environments to install specific versions of packages.

#---------------Search packages in pip------------------------
#The search command is used to search for packages
# Command Line: pip search pygame

