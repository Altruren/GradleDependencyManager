from FileReader import FileReader


class FilePropertyUpdater:
    def __init__(self, fileName):
        self.file = fileName
        self.fileReader = FileReader(self.file)

    def update(self, strategy):
        lines = self.fileReader.getFileLines()
        newFileString = strategy.build(lines)
        self.writeToFile(newFileString)

    def writeToFile(self, newFileString):
        fileToWriteTo = open(self.file, 'w')
        fileToWriteTo.write(newFileString)
        fileToWriteTo.close()
