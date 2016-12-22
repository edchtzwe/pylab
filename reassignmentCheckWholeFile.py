# declaration finder for PERL, find the occurences of a my declaration of a variable
# 09 Dec 2016
# Edmund Chong / 7440820@gmail.com
import os;
import re;
from lib import App;
from lib import lineNumAndText;

progName = os.path.basename(__file__);
print "progName = " + progName;
initInstances = App.genericInitOperation("variable");
filePath = initInstances['filePath'];
originalFilePath = 0;
resetModeName = 0;
startLine = 0;
endLine = 0;
varName = initInstances['modeName'];

while (True):
    if (resetModeName):
        varName = App.getModeName('Variable');
        resetModeName = 0;
    # term can look like
    # my $term =
    # my ($term, ...)
    # my ($other, $term, ....) or my ( $other, $term, ....)
    lineNum = [];
    lineText = [];

     # we are assuming you're a good programmer that you my or our your PERL variables
    # we are only checking for re-assignments varName = newValue;
    regex = re.compile('(\$|@|%)'+varName+'(\,|\))?\s*(\$.*\)*)*\.?=');
    # we do not want any declarations, for PERL, skip any lines with a my declaration keyword
    # add our if you want, but globals are pretty nasty so we're not using those
    regex2 = re.compile('my\s+'); # at least a space between my or else it's malformed
    try:
        fileHandler = open(filePath, "r");
    except:
        print "Failed to open file. Using last provided file: " + originalFilePath;
        filePath = originalFilePath;
        fileHandler = open(filePath, "r");

    result = lineNumAndText.reassignmentCheck(fileHandler, regex, regex2);
    fileHandler.close();
    App.genericPrintResults(result);
    
    reinitSequence = App.reinitSequenceNoScope(initInstances);
    initInstances['filePath'] = reinitSequence['filePath'];
    resetModeName = reinitSequence['resetModeName'];
    filePath = reinitSequence['filePath'];