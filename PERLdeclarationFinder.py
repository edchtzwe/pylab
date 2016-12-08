# declaration finder for PERL, find the occurences of a my declaration of a variable
# 08 Dec 2016; Edmund Chong
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
while (True):
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
    # term can look like
    # my $term =
    # my ($term, ...)
    # my ($other, $term, ....) or my ( $other, $term, ....)
    lineNum = [];
    lineText = [];
    regex = re.compile('my.*(\$|@|%)'+varName+'[,\s\)].*=');
    # if in a foreach my $varName 
    regex2 = re.compile('foreach\s*my\s\$'+varName+'.*');
    # my $var;
    regex3 = re.compile('my.*(\$|@|%)'+varName+'\)*;');
    # LHS check
    regex4 = re.compile('my.*(\$|@|%)'+varName+'\)*');
    with open(filePath, "r") as fileHandler:
        for line_i, line in enumerate(fileHandler, 1):
            assgn = line.split('=');
            assgnChk = 0;
            # it's an assign, check LHS only
            if len(assgn) > 1:
                line = assgn[0];
                assgnChk = regex4.search(line);
            if (regex.search(line) or regex2.search(line) or regex3.search(line) or assgnChk) and line_i >= int(startLine):
                if endLine < 1:
                    if len(assgn) > 1:
                        lineNum.append(str(line_i));
                        lineText.append(assgn[0] + " = " + assgn[1]);
                    else:
                        lineNum.append(str(line_i));
                        lineText.append(line);
                else:
                    if line_i > endLine:
                        continue;
                    else:
                        if len(assgn) > 1:
                            lineNum.append(str(line_i));
                            lineText.append(assgn[0] + " = " + assgn[1]);
                        else:
                            lineNum.append(str(line_i));
                            lineText.append(line);
        fileHandler.close();
    print "line num\tline text";
    for index in range(len(lineNum)):            
        print lineNum[index] + " | " + lineText[index].strip();
    
    print "New file?(1 or 0):";
    newFile = 0;
    try:
        newFile = int(raw_input());
    except:
        newFile = 0;
    if newFile > 0:
        print "Filename:";
        fileName = raw_input();
        filePath = folderPath + fileName;