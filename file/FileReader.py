class FileReader:
    def __init__(self, file):
        self.file = file

    def getFileLines(self):
        fileToRetrieveFrom = open(self.file, 'r')
        lines = fileToRetrieveFrom.readlines()
        fileToRetrieveFrom.close()
        return lines
