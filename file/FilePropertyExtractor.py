from FileReader import FileReader


class FilePropertyExtractor:
    def __init__(self, fileName):
        self.file = fileName
        self.fileReader = FileReader(self.file)

    def getPropertyFromFile(self, itemToExtract, strategy):
        return self.extractItemFromLines(self.fileReader.getFileLines(), itemToExtract, strategy)

    def extractItemFromLines(self, lines, itemToExtract, strategy):
        return strategy.extract(lines, itemToExtract)
