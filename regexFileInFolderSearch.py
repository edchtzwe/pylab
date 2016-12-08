# regex file in folder search
# 09 Dec 2016
# Edmund Chong

import os;
import re;

progName = os.path.basename(__file__);
print "progName = " + progName;
curDir = os.path.dirname(__file__);
relPath = "/folderPath.txt";
curDir = curDir.replace("\\", "/");
folderPath = open(curDir+relPath, "r");
folderPath = folderPath.read();
print "Regex string: ";
pattern = raw_input();
regex = re.compile(pattern);
print "Searching :" + folderPath + " for " + pattern;
pathlist = os.listdir(folderPath);
lineNum = [];
lineText = [];

# run through every file in the folder
for index in range(len(pathlist)):    
    # get the fileName and append to the folderPath, forming a filePath
    filePath = folderPath+pathlist[index];
    with open(filePath, "r") as fileHandler:
        for line_i, line in enumerate(fileHandler, 1):
            if (regex.search(line)):
                print filePath + " => " + str(line_i) + " | " + line;
        fileHandler.close();
