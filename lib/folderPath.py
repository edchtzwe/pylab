import os;

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
    return folderPath
    