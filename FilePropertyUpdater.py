from FileReader import FileReader


class FilePropertyUpdater:
    def __init__(self, fileName):
        self.file = fileName
        self.fileReader = FileReader(self.file)

    def updateProperty(self, strategy, newFileName):
        lines = self.fileReader.getFileLines()
        newFileString = strategy.build(lines)
        self.writeToFile(newFileName, newFileString)

    def writeToFile(self, fileName, newFileString):
        fileToWriteTo = open(fileName, 'w')
        fileToWriteTo.write(newFileString)
        fileToWriteTo.close()
