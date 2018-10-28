####
# Started from some folder $F, it will check in the resources subfolder to find
# 1.txt, 2.txt, ... 6.txt, concatenate the files and write them to
# a file named yyyy-MM-dd.txt for the current datetime.

import os.path
from os import listdir
from os.path import isfile, join
import datetime
import argparse
import sys


outputdirectory = 'created'
directory = 'resources'
headernames = ['THE PRACTICE OF ' + x for x in
               ['LIVING CONSCIOUSLY', 'SELF-ACCEPTANCE', 'SELF-RESPONSIBILITY',
                'SELF-ASSERTIVENESS', 'LIVING PURPOSEFULLY', 'PERSONAL INTEGRITY']]

# helper methods
def parseFileNameToObject(name):
    parts = name.split('_')
    habit = int(parts[0][0])
    week = ''
    timeofday = 1

    for i in range(1, len(parts)):
        if (parts[i].find("morning") != -1):
            timeofday = 1
            continue
        if (parts[i].find("evening") != -1):
            timeofday = 0
            continue
        if (parts[i].find("week") != -1):
            week = parts[i][4:]
            continue

    return (habit, week, timeofday)

# inside resources the files should be named 1.txt, 2.txt, ..., 6.txt for each
# respective habit.

#########################################################################
## CODE

print(sys.argv[1:])

# parse arguments
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('habits', metavar='habits', type=int, nargs='+',
                    help='the desired practices you want to include')
parser.add_argument('--week', help='e.g. 1st week you are doing, put in 1. 2nd week, put in 2...')
parser.add_argument('--morning', help="if it's morning put in 1, else 0.")

args = parser.parse_args()


if os.path.isdir(directory):

    # get all files
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    onlyfiles.sort()

    ### filter only those that we want
    A = [(parseFileNameToObject(f), directory + '/' + f) for f in onlyfiles]
    # filter by habits
    A = [x for x in A if x[0][0] in args.habits]
    # filter by week
    B = []
    for x in A:
        if x[0][1].find('+') != -1:
            if int(x[0][1][0]) <= int(args.week):
                B.append(x)
        else:
            if x[0][1] == args.week:
                B.append(x)
            if x[0][1] == '':
                B.append(x)
    A = B
    # filter by part of day
    A = [x for x in A if x[0][2] == int(args.morning)]

    # write to file
    allcontent = ''

    for i in range(len(A)):

        content = open(A[i][1], 'r').read()
        allcontent += headernames[A[i][0][0] - 1] + '\n\n'
        allcontent += content
        allcontent += '\n\n'

    resultfilename = str(datetime.datetime.now().strftime('%Y-%m-%d')) + '.md'

    open(outputdirectory + "/" + resultfilename, 'w').write(allcontent)
