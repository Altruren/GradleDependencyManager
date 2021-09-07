from FileReader import FileReader
from GradleProperty import GradleProperty


class FilePropertyUpdater:
    def __init__(self, fileName):
        self.file = fileName
        self.fileReader = FileReader(self.file)

    def updateProperty(self, dependencyToUpdate, newVersion, newFile):
        lines = self.fileReader.getFileLines()
        newFileString = self.buildNewFile(lines, dependencyToUpdate, newVersion)
        self.writeToFile(newFile, newFileString)

    def buildNewFile(self, lines, dependencyToUpdate, newVersion):
        newFileString = ""
        for line in lines:
            lineToAdd = line
            if dependencyToUpdate in line:
                lineToAdd = self.buildGradleProperty(line, newVersion)
            newFileString += lineToAdd
        return newFileString

    def buildGradleProperty(self, line, newVersion):
        propertySeparator = "="
        dependencySeparator = ":"
        propertySplit = line.split(propertySeparator)
        propertyName = propertySplit[0]
        propertyDefinition = propertySplit[1]
        dependencySplit = propertyDefinition.split(dependencySeparator)
        module = dependencySplit[0]
        group = dependencySplit[1]

        gradleProperty = GradleProperty(propertyName, module, group, newVersion)

        return str(gradleProperty)

    def writeToFile(self, fileName, newFileString):
        fileToWriteTo = open(fileName, 'w')
        fileToWriteTo.write(newFileString)
        fileToWriteTo.close()
