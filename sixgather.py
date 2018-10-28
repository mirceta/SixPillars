import os.path
from os import listdir
from os.path import isfile, join
from datetime import datetime, timedelta
from collections import defaultdict

# variables
inputdirectory = 'created'
directory = 'resources'

# methods
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

#############################################
## CODE

# get current datetime
startdate = datetime.now().strftime('%Y-%m-%d')
currentdate = datetime.now()


# get six pillars journal files contents for last 7 days
query = []
for i in range(1,8):
    currentdate = currentdate - timedelta(days=1)
    query.append(currentdate.strftime('%Y-%m-%d') + '.md')

journalfilenames = [f for f in listdir(inputdirectory) if isfile(inputdirectory + "/" + f) and f.find('.md') != -1]
journals = []
for f in journalfilenames:
    journals.append(open(inputdirectory + '/' + f, 'r').readlines())


# get all resource file contents, questions. Accumulate in the form hash[PRACTICE][QUESTION] = list(answers)
resourcefilenames = [f for f in listdir(directory) if isfile(join(directory, f))]
resourcefilenames.sort()

headernames = ['THE PRACTICE OF ' + x for x in
               ['LIVING CONSCIOUSLY', 'SELF-ACCEPTANCE', 'SELF-RESPONSIBILITY',
                'SELF-ASSERTIVENESS', 'LIVING PURPOSEFULLY', 'PERSONAL INTEGRITY']]


# put all those that have the same practice into the same array
resourcefilecontentlist = [(parseFileNameToObject(f)[0], [line.rstrip() for line in open(directory + "/" + f, 'r').readlines()]) for f in resourcefilenames]
practice_to_content_map = defaultdict(list)
for o in resourcefilecontentlist:
    practice_to_content_map[o[0]].extend(o[1])
keys = [k for k in practice_to_content_map.keys()]
keys.sort()
resourcefilecontentlist = [practice_to_content_map[k] for k in keys]




accumulator = {k: {l: list() for l in v} for k, v in zip(headernames, resourcefilecontentlist)}

## fill up the accumulator
journals = [[k.rstrip() for k in j] for j in journals]
for journal in journals:
    currentheadername = ''
    currentquestion = ''
    for line in journal:
        if line in ['', ' ', '\n']:
            continue
        if line in headernames:
            currentheadername = line
            continue
        if line in accumulator[currentheadername]:
            currentquestion = line
            continue
        accumulator[currentheadername][currentquestion].append(line)

## aggregate the results into a string
resultfilecontent = ''
for header in accumulator.keys():
    resultfilecontent += "## " + header + "\n\n"
    for question in accumulator[header].keys():
        if len(accumulator[header][question]) > 0:
            resultfilecontent += "### " + question + "\n\n"
            resultfilecontent += '\n'.join(accumulator[header][question])
            resultfilecontent += '\n\n'

open('gathered/endofweek_' + startdate + '.md', 'w').write(resultfilecontent)