
"""This module reads in a csv file, removes the commas and replaces them with spaces creating a text file.
    It takes two args: the path to the original csv file and the path where you want to put the new txt file."""

import sys 
import csv
import getopt

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
        
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error as msg:
            raise Usage(msg)
    
    except Usage as err:
        print >>sys.stderr, err.msg
        
    csvfile = args[0]    
    textfile = args[1]
    
    #open csv file for reading
    try:
        reader = csv.reader(open(csvfile), dialect='excel', quoting=csv.QUOTE_NONE)
    except IOError as ioe:
        print('Cannot open file: ' + str(ioe))
    except csv.Error as csve:
        print('Cannot open file: ' + str(csve))

    #open text file for writing 
    try:
        newfile = open(textfile, 'w')
        print("Creating new file...")
        for row in reader:
            line = ' '.join(row)
            newfile.write(line + "\n")
        newfile.close()
        print("New file created.")
    except IOError as e:
        print('Cannot open file: ' + str(e))

if __name__ == '__main__':
    sys.exit(main())
