# variable usage finder.
# 12 Dec 2016
# Edmund Chong / 7440820@gmail.com
import os;
import re;
from lib import App;
from lib import lineNumAndText;

progName = os.path.basename(__file__);
print "progName = " + progName;

initInstances = App.scopedInitOperation("variable");
regex0 = re.compile('[\$|@|%|@\$|@\{\$]' + initInstances['modeName'] + '[,|\s*|\);=-]');
regexList = [regex0];
filePath = initInstances['filePath'];
originalFilePath = 0;
resetLineNum = 0;
resetModeName = 0;
startLine = 0;
endLine = 0;
varName = initInstances['modeName'];

while(True):
    if (resetLineNum):
        scope = lineNumAndText.getScope();
        startLine = scope['startLine'];
        endLine = scope['endLine'];
        resetLineNum = 0;
    if (resetModeName):
        varName = App.getModeName('Variable');
        resetModeName = 0;
    fileHandler = open(initInstances['filePath'], "r");
    result = lineNumAndText.scopedLineNumAndText(fileHandler, regexList, initInstances['scope']);

    fileHandler.close();

    App.genericPrintResults(result);
    
    reinitSequence = App.genericReinitSequence(initInstances);
    initInstances['filePath'] = reinitSequence['filePath'];
    resetModeName = reinitSequence['resetModeName'];
    filePath = reinitSequence['filePath'];
    resetLineNum = reinitSequence['resetLineNum'];