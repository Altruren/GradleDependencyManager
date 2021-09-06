class FileExtractor:
    def __init__(self, fileName):
        self.file = fileName

    def getItemFromFile(self, itemToRetrieve, splitter):
        return self.extractItemFromLines(self.getFileLines(), itemToRetrieve, splitter)

    def getFileLines(self):
        fileToRetrieveFrom = open(self.file, 'r')
        lines = fileToRetrieveFrom.readlines()
        fileToRetrieveFrom.close()
        return lines

    def extractItemFromLines(self, lines, idToFind, splitter):
        for line in lines:
            if line.startswith(idToFind):
                split = line.split(splitter)
                return split[1].strip("\n")
