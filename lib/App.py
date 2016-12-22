import os;
from lib import lineNumAndText;

def getFolderPath():
    curDir = os.path.dirname(__file__);
    relPath = "/folderPath.txt";
    curDir = curDir.replace("\\", "/");
    folderPath = open(curDir+relPath, "r");
    folderPath = folderPath.read();
    flag0 = 0; # 0 for cgi-bin, 1 for lib
    flag1 = 0; # 1 to quit at first match. 0 runs through the whole file
    folderList = ["cgi-bin/", "lib/"];
    folder = folderList[0];
    print "cgi-bin or lib? (0 or 1):"
    try:
        flag0 = int(raw_input());
    except:
        flag0 = 0;
    if flag0:
        folder = folderList[1];
    folderPath = folderPath + folder;
    return folderPath;
    
def getModeName(mode):
    print mode + " name:";
    modeName = raw_input();
    return modeName;
    
def genericInitOperation(mode):
    folderPath = getFolderPath();

    print "Filename:";
    fileName = raw_input();
    filePath = folderPath + fileName;
    scope = {'startLine':0, 'endLine':0}
    modeName = getModeName(mode);
    print "Searching " + modeName + " in " + filePath;
    
    return {'folderPath':folderPath, 'filePath':filePath, 'modeName':modeName, 'mode':mode, 'scope':scope};
    
def scopedInitOperation(mode):
    folderPath = getFolderPath();

    print "Filename:";
    fileName = raw_input();
    filePath = folderPath + fileName;
    scope = lineNumAndText.getScope();
    modeName = getModeName(mode);
    
    return {'folderPath':folderPath, 'filePath':filePath, 'modeName':modeName, 'mode':mode, 'scope':scope};
    
def genericPrintResults(result):
    lineNum = result['lineNum'];
    lineText = result['lineText'];
    print "line num\tline text";
    for index in range(len(lineNum)):
        print lineNum[index] + " | " + lineText[index].strip();

def genericReinitSequence(initInstances):
    print "New file?(1 or 0):";
    newFile = 0;
    folderPath = initInstances['folderPath'];
    filePath = initInstances['filePath'];
    resetLineNum = 0;
    resetModeName = 0;
    
    try:
        newFile = int(raw_input());
    except:
        newFile = 0;
        
    print "Reset scope?(1 or 0):";
    try:
        resetLineNum = int(raw_input());
    except:
        resetLineNum = 0;

    print "Reset " + initInstances['mode'] + "? (1 or 0):";
    try:
        resetModeName = int(raw_input());
    except:
        resetModeName = 0;
        
    if newFile > 0:
        print "Filename:";
        fileName = raw_input();
        filePath = folderPath + fileName;
        
    return {'resetLineNum':resetLineNum, 'filePath':filePath, 'resetModeName':resetModeName};
    
def reinitSequenceNoScope(initInstances):
    print "New file?(1 or 0):";
    newFile = 0;
    folderPath = initInstances['folderPath'];
    filePath = initInstances['filePath'];
    resetLineNum = 0;
    resetModeName = 0;
    
    try:
        newFile = int(raw_input());
    except:
        newFile = 0;

    print "Reset " + initInstances['mode'] + "? (1 or 0):";
    try:
        resetModeName = int(raw_input());
    except:
        resetModeName = 0;
        
    if newFile > 0:
        print "Filename:";
        fileName = raw_input();
        filePath = folderPath + fileName;
        
    return {'filePath':filePath, 'resetModeName':resetModeName};