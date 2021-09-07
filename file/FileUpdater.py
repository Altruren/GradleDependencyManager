from FileReader import FileReader


class FileUpdater:
    def __init__(self, fileName):
        self.file = fileName
        self.fileReader = FileReader(self.file)

    def update(self, strategy):
        lines = self.fileReader.getFileLines()
        updatedFileString = strategy.build(lines)
        self.writeToFile(updatedFileString)

    def writeToFile(self, updatedFileString):
        fileToWriteTo = open(self.file, 'w')
        fileToWriteTo.write(updatedFileString)
        fileToWriteTo.close()
