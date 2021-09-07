from FileReader import FileReader


class FilePropertyExtractor:
    def __init__(self, fileName):
        self.file = fileName
        self.fileReader = FileReader(self.file)

    def getPropertyFromFile(self, strategy):
        return strategy.extract(self.fileReader.getFileLines())
