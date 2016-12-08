import os;
import re;

progName = os.path.basename(__file__);
print "progName = " + progName;
curDir = os.path.dirname(__file__);
relPath = "/folderPath.txt";
curDir = curDir.replace("\\", "/");
folderPath = open(curDir+relPath, "r");
folderPath = folderPath.read();
print "Searching :" + folderPath;
pathlist = os.listdir(folderPath);
withStr = [];
withoutStr = [];
for index in range(len(pathlist)):    
    filePath = folderPath+pathlist[index];
    fileHandler = open(filePath, "r");
    fileContents = fileHandler.read()
    regex = re.search(r'(main)\s*\(', fileContents);
    # withStr.append(filePath) if regex != None else withoutStr.append(filePath);
    if not regex:
        print filePath;
    fileHandler.close();
# print "\n".join(withStr);
