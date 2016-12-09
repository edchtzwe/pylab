# checks for re-assginment within the same scope
# 09 Dec 2016
# Edmund Chong / 7440820@gmail.com

import os;
import re;

progName = os.path.basename(__file__);
print "progName = " + progName;
curDir = os.path.dirname(__file__);
relPath = "/folderPath.txt";
curDir = curDir.replace("\\", "/");
# folder path holds the fullpath to the folder to be search eg. c://tier1/tier2/
folderPath = open(curDir+relPath, "r");
print "Filename:";
fileName = raw_input();
folderPath = folderPath.read()
filePath = folderPath + fileName;
originalFilePath = 0;
resetLineNum = 1;
startLine = 0;
endLine = 0;
# main loop. Refactor to main() if free.
while (True):
    if (resetLineNum):
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
    print "Varname:";
    varName = raw_input();
    print "Searching " + varName + " in " + filePath;
    lineNum = [];
    lineText = [];
    # we are assuming you're a good programmer that you my or our your PERL variables
    # we are only checking for re-assignments varName = newValue;
    regex = re.compile('(\$|@|%)'+varName+'(\,|\))?\s*(\$.*\)*)*=');
    # we do not want any declarations, for PERL, skip any lines with a my declaration keyword
    # add our if you want, but globals are pretty nasty so we're not using those
    regex2 = re.compile('my\s+'); # at least a space between my or else it's malformed
    try:
        fileHandler = open(filePath, "r");
    except:
        print "Failed to open file. Using last provided file: " + originalFilePath;
        filePath = originalFilePath;
        fileHandler = open(filePath, "r");
    for line_i, line in enumerate(fileHandler, 1):
        if (regex2.search(line)):
            continue;
        else :
            if (regex.search(line)) and line_i >= int(startLine):
                if endLine < 1:
                    lineNum.append(str(line_i));
                    lineText.append(line);
                else:
                    if line_i > endLine:
                        continue;
                    else:
                        lineNum.append(str(line_i));
                        lineText.append(line);
    fileHandler.close();
    print "line num\tline text";
    for index in range(len(lineNum)):            
        print lineNum[index] + " | " + lineText[index].strip();
    
    print "New file?(1 or 0):";
    newFile = 0;
    # if we got here, everything has been working perfectly
    originalFilePath = filePath;
    try:
        newFile = int(raw_input());
    except:
        newFile = 0;
    print "Reset scope?(1 or 0):";
    try:
        resetLineNum = int(raw_input());
    except:
        resetLineNum = 0;
    if newFile > 0:
        print "Filename:";
        fileName = raw_input();
        filePath = folderPath + fileName;