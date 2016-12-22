# declaration finder for PERL, find the occurences of a my declaration of a variable
# 09 Dec 2016
# Edmund Chong / 7440820@gmail.com
import os;
import re;
from lib import App;
from lib import lineNumAndText;

progName = os.path.basename(__file__);
print "progName = " + progName;
initInstances = App.scopedInitOperation("variable");
filePath = initInstances['filePath'];
originalFilePath = 0;
resetLineNum = 0;
resetModeName = 0;
startLine = 0;
endLine = 0;
varName = initInstances['modeName'];

while (True):
    if (resetLineNum):
        scope = lineNumAndText.getScope();
        initInstances['scope']['startLine'] = scope['startLine'];
        initInstances['scope']['endLine'] = scope['endLine'];
        resetLineNum = 0;
    if (resetModeName):
        varName = App.getModeName('Variable');
        resetModeName = 0;
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
    regex4 = re.compile('my.*(\$|@|%)'+varName+'[,\)\s*]');
    regexList = [regex, regex2, regex3, regex4];
    try:
        fileHandler = open(filePath, "r");
    except:
        print "Failed to open file. Using last provided file: " + originalFilePath;
        filePath = originalFilePath;
        fileHandler = open(filePath, "r");

    result = lineNumAndText.scopedAssignCheckLineNumAndText(fileHandler, regexList, initInstances['scope']);
    fileHandler.close();
    
    App.genericPrintResults(result);
    
    reinitSequence = App.genericReinitSequence(initInstances);
    initInstances['filePath'] = reinitSequence['filePath'];
    resetModeName = reinitSequence['resetModeName'];
    filePath = reinitSequence['filePath'];
    resetLineNum = reinitSequence['resetLineNum'];
    