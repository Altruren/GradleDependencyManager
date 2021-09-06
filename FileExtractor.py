class FileExtractor:
    def __init__(self, fileName, strategy):
        self.file = fileName
        self.strategy = strategy

    def getPropertyFromFile(self, itemToExtract):
        return self.extractItemFromLines(self.getFileLines(), self.strategy, itemToExtract)

    def getFileLines(self):
        fileToRetrieveFrom = open(self.file, 'r')
        lines = fileToRetrieveFrom.readlines()
        fileToRetrieveFrom.close()
        return lines

    def extractItemFromLines(self, lines, strategy, itemToExtract):
        return strategy.extract(lines, itemToExtract)
