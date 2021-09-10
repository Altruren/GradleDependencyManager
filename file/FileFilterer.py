from file.FileReader import FileReader


class FileFilterer:
    def filterFilesWithValidName(self, fileList):
        gradleFiles = []
        validFiles = self.getValidFileNames()
        for element in fileList:
            if element in validFiles:
                gradleFiles.append(element)
        return gradleFiles

    def getValidFileNames(self):
        validFilesPath = "./validFiles.txt"
        fileReader = FileReader(validFilesPath)
        validFileNames = []
        for line in fileReader.getFileLines():
            validFileNames.append(line.strip("\n"))
        return validFileNames