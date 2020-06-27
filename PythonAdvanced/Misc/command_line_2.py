#GetOpt Module
#Python getopt module is similar to the getopt() function of C. Unlike sys module getopt
# module extends the separation of the input string by parameter validation. It allows both
# short, and long options including a value assignment.
# However, this module requires the use of the sys module to process input data properly.
# To use getopt module, it is required to remove the first element from the
# list of command-line arguments.

import getopt, sys

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]
# Options
options = "hmo:"
# Long options
long_options = ["Help", "My_file", "Output ="]
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
    # checking each argument
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--Help"):
            print("Diplaying Help")
        elif currentArgument in ("-m", "--My_file"):
            print("Displaying file_name:", sys.argv[0])
        elif currentArgument in ("-o", "--Output"):
            print(("Enabling special output mode (% s)") % (currentValue))
except getopt.error as err:
    # output error, and return with an error code
    print(str(err))

#To run this try the below options on command line
#python command_line_2.py -h
#python command_line_2.py -m
#python command_line_2.py -hm
