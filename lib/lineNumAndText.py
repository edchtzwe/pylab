import os;
import re;

def genericLineNumAndText(fileHandler, regexList):
    lineNum = [];
    lineText = [];
    for line_i, line in enumerate(fileHandler, 1):
        if (regexCheck(regexList, line)):
            lineNum.append(str(line_i));
            lineText.append(line);
    return {'lineNum':lineNum, 'lineText':lineText};

def regexCheck(regexList, line):
    for index in range(len(regexList)):
        if (regexList[index].search(line)):
            return 1;
    return 0;
    
def getScope():
    print "After line num:"
    startLine = 0;
    endLine = 0;
    try:
        startLine = int(raw_input());
    except:
        startLine = 1;
    print "End line num (0 to skip):";
    try:
        endLine = int(raw_input());
    except:
        endLine = 0;
    return {'startLine':startLine, 'endLine':endLine};