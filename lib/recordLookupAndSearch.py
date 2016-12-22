import os;

def Search(fileHandler, term):
    fileContents = fileHandler.read();
    contentArray = fileContents.split(',');
    contentArray = [temp.lower() for temp in contentArray];
    for fileName in contentArray:
        # print fileName;
        if fileName == term.lower():
            return 1;
    return 0;
    
def Save(fileHandler, term):
    fileContents = fileHandler.read();
    # print fileContents;
    fileHandler.write(term + ",");
    
def ShowAll(fileHandler):
    fileContents = fileHandler.read();
    contentArray = fileContents.split(',');
    contentArray.sort();
    return contentArray;
    
def PrintToFile(fileName, contentArray):
    fileHandler = open(getFolderPath(fileName), "w");
    contentArray.sort();
    print "csv|newline?(0|1)";
    flag0 = 0;
    try:
        flag0 = int(raw_input());
    except:
        flag0 = 0;
    if (not flag0):
        contentArray = ','.join(contentArray);
    else:
        contentArray = '\n'.join(contentArray);
    fileHandler.write(contentArray);
    fileHandler.close();
    
def getFolderPath(fileName):
    curDir = os.path.dirname(__file__);
    relPath = "/"+fileName;
    curDir = curDir.replace("\\", "/");
    folderPath = curDir+relPath;
    return folderPath;
    
def ArraySearch(contentArray, term):
    contentArray = [temp.lower() for temp in contentArray];
    for fileName in contentArray:
        # print fileName;
        if fileName == term.lower():
            return 1;
    return 0;

def cleanRecord(fileHandler):
    fileContents = fileHandler.read();
    contentArray = fileContents.split(',');
    contentArray = [temp.lower() for temp in contentArray];
    contentArray2 = [];
    contentArray2.append(contentArray.pop(0));
    count = 0;
    for file in contentArray:
        count+=1;
        # add into contentArray2 if not already in contentArray2
        # print contentArray;
        if (not ArraySearch(contentArray2, file)):
            contentArray2.append(file);
    PrintToFile("records2.txt", contentArray2);
    print "Total: " + str(count);