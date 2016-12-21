# Record lookup and save
# 21 Dec 2016
# Edmund Chong / 7440820@gmail.com
from lib import recordLookupAndSearch;

print "Clean records? (0|1)"
try:
    prompt = int(raw_input());
except:
    prompt = 0;

if (prompt):
    fileHandler = open(recordLookupAndSearch.getFolderPath("records.txt"), "r+");
    recordLookupAndSearch.cleanRecord(fileHandler);
    
while (True):
    # determine if saving to file or searching
    print "Search, Save? (0, 1)";
    flag0 = 0;
    flag2 = 0;
    try:
        flag0 = int(raw_input());
    except:
        flag0 = 0;
    # saving, so open file, read, sort, then write
    if (not flag0):
        # searching, get user input
        fileHandler = open(recordLookupAndSearch.getFolderPath("records.txt"), "r+");
        print "Term to search.";
        term = raw_input();
        # found, say found
        if (recordLookupAndSearch.Search(fileHandler, term)):
            print term + " found.";
        else:
            # missing, ask if saving
            print "Term not found. Save " + term + "?(0 or 1)";
            flag1 = 0;
            try:
                flag1 = int(raw_input());
            except:
                flag1 = 0;
            if (flag1):
                recordLookupAndSearch.Save(fileHandler, term);
        fileHandler.close();
    elif (flag0 == 1):
        fileHandler = open(recordLookupAndSearch.getFolderPath("records.txt"), "r+");
        # saving, call saving
        print "Term to save.";
        term = raw_input();
        # fileHandler.read();
        if (not recordLookupAndSearch.Search(fileHandler, term)):
            recordLookupAndSearch.Save(fileHandler, term);
        else:
            print "Duplicate, not saved.";
        fileHandler.close();
    else :
        fileHandler = open(recordLookupAndSearch.getFolderPath("records.txt"), "r");
        contentArray = recordLookupAndSearch.ShowAll(fileHandler);
        content = [temp for temp in contentArray if temp];
        for file in content:
            print file;
        fileHandler.close();

    # repeat
