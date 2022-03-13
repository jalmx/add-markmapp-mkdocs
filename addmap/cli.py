import argparse
import logging

# options
# path = path where existe folder docs and file config yml
# exclude = paths to excludes, default 
# flag_to_insert = 
# clear = delete the map from file



"""All logical to create a cli with options to run
    """

verbose = False

def main():
    parser = argparse.ArgumentParser(description="Command to add markmap to index to all folders, search all index.md with a flag where insert information" )
    parser.add_argument('-p',"--path", help="Path from folder to have inside docs folder. Default: Here (.)",default=".")
    parser.add_argument('-v','--verbose',help="Show all logs", action="store_true")
    parser.add_argument('-e','--exclude',metavar="paths/to/exclude",  help="Exclude directories or folders inside PATH. Ex: -e path/to/exclude path/to/exclude2", nargs="+" )
    
    
    argument = parser.parse_args()
    
    verbose = argument.verbose
    
    print("Path",argument.path)
    print("Exclude",argument.exclude)
    

if __name__ == "__main__":
    main()
    
# https://realpython.com/command-line-interfaces-python-argparse/
# https://docs.python.org/3/library/argparse.html#module-argparse
# https://betterprogramming.pub/python-click-building-your-first-command-line-interface-application-6947d5319ef7