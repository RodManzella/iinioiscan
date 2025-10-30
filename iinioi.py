import argparse
import sys
import subprocess
import requestsLoop
import readStdin
import checkPath
from logo import print_logo


parser = argparse.ArgumentParser(
    prog='script.py'
)
parser.add_argument("-p", "--path", metavar="",help="Specify path to file")
parser.add_argument("-u", "--url", metavar="",help="Specify url to check")
args = parser.parse_args()



def print_logo_and_path():
    print_logo()
    parser.print_help()

if(len(sys.argv) == 1 and sys.stdin.isatty()):  # sem stdin
    print_logo_and_path()

    
if(len(sys.argv) == 1 and not sys.stdin.isatty()): # com stdin
    print_logo()
    stdInput = sys.stdin.read()
    readStdin.readStdinLines(stdInput)


if(args.path):
    print_logo()
    checkPath.iterateFile(args.path)

