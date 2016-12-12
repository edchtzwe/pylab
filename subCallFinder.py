# subroutine call finders. To check parameter passing
# 12 Dec 2016
# Edmund Chong / 7440820@gmail.com
import os;
import re;
from lib import folderPath;
from lib import lineNumAndText;

progName = os.path.basename(__file__);
print "progName = " + progName;
folderPath = folderPath.getFolderPath();

print "Filename:";
fileName = raw_input();
filePath = folderPath + fileName;

print "Sub name:";
subName = raw_input();
print "Searching " + subName + " in " + filePath;

regex0 = re.compile('[\s*|\&]' + subName + '\s*');
regexList = [regex0];

fileHandler = open(filePath, "r");

result = lineNumAndText.genericLineNumAndText(fileHandler, regexList);
lineNum = result['lineNum'];
lineText = result['lineText'];

fileHandler.close();

print "line num\tline text";
for index in range(len(lineNum)):            
    print lineNum[index] + " | " + lineText[index].strip();