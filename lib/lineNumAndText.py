import os;
import re;

getNextRegex = re.compile('\S*\s*;');

def genericLineNumAndText(fileHandler, regexList):
    lineNum = [];
    lineText = [];
    for line_i, line in enumerate(fileHandler, 1):
        if (regexCheck(regexList, line)):
            lineNum.append(str(line_i));
            lineText.append(line);
    return {'lineNum':lineNum, 'lineText':lineText};
    
def scopedLineNumAndText(fileHandler, regexList, scope):
    lineNum = [];
    lineText = [];
    startLine = scope['startLine'];
    endLine = scope['endLine'];
    getNext = 0;
    for line_i, line in enumerate(fileHandler, 1):
        if (getNext):
            lineNum.append('   ');
            lineText.append(line);
        if (getNextRegex.search(line)):
            getNext = 0;
        if (startLine and line_i < startLine):
            continue;
        if (endLine and line_i > endLine):
            break;
        if (regexCheck(regexList, line)):
            lineNum.append(str(line_i));
            lineText.append(line);
            if (not getNextRegex.search(line)):
                getNext = 1;
    return {'lineNum':lineNum, 'lineText':lineText};
    
# only checks LHS if variable is found in an assignment statement
def scopedAssignCheckLineNumAndText(fileHandler, regexList, scope):
    lineNum = [];
    lineText = [];
    startLine = scope['startLine'];
    endLine = scope['endLine'];
    getNext = 0;
    
    for line_i, line in enumerate(fileHandler, 1):
        originalLine = line;
        if (getNext):
            lineNum.append('   ');
            lineText.append(line);
        if (getNextRegex.search(originalLine)):
            getNext = 0;
        if (startLine and line_i < startLine):
            continue;
        if (endLine and line_i > endLine):
            break;
        assgn = line.split('=');
        
        # it's an assign, check LHS only
        if len(assgn) > 1:
            line = assgn[0];
        
        if (regexCheck(regexList, line)):
            lineNum.append(str(line_i));
            lineText.append(originalLine);
            if (not getNextRegex.search(originalLine)):
                getNext = 1;
    return {'lineNum':lineNum, 'lineText':lineText};
    
def reassignmentCheck(fileHandler, regex, regex2):
    lineNum = [];
    lineText = [];
    for line_i, line in enumerate(fileHandler, 1):
        if (regex2.search(line)):
            continue;
        else :
            if (regex.search(line)):
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
    