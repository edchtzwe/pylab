# regex file in folder search
# 09 Dec 2016
# Edmund Chong / 7440820@gmail.com

import os;
import re;
from lib import folderPath;

progName = os.path.basename(__file__);
print "progName = " + progName;
folderPath = folderPath.getFolderPath();

print "Quit at first match in file? (0 or 1):"
try:
    flag1 = int(raw_input());
except:
    flag1 = 0;
    
print "Regex string: ";
pattern = raw_input();
regex = re.compile(pattern);
print "Searching :" + folderPath + " for " + pattern;
pathlist = os.listdir(folderPath);

# run through every file in the folder
for index in range(len(pathlist)):    
    # get the fileName and append to the folderPath, forming a filePath
    filePath = folderPath+pathlist[index];
    try:
        fileHandler = open(filePath, "r");
        for line_i, line in enumerate(fileHandler, 1):
            if (regex.search(line)):
                print filePath + " => " + str(line_i) + " | " + line;
                if (flag1):
                    break;
        fileHandler.close();
    except:
        continue;
