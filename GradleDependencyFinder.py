import os

from file.FileReader import FileReader


class GradleDependencyFinder:
    def __init__(self, parentDirectory, dependencyToFind):
        self.parentDirectory = parentDirectory
        self.dependencyToFind = dependencyToFind

    def findGradleFilesWithDependency(self, dependency):
        gradleFiles = self.findAllGradleFiles()
        return self.filterGradleFilesThatHaveDependency(gradleFiles, dependency)

    def findAllGradleFiles(self):
        fileList = os.listdir(self.parentDirectory)
        return self.getGradleFiles(fileList)

    def getGradleFiles(self, fileList):
        gradleFiles = []
        for file in fileList:
            if file == "build.gradle" or file == "gradle.properties":
                gradleFiles.append(file)
        return gradleFiles

    def filterGradleFilesThatHaveDependency(self, gradleFiles, dependencyToFilterOn):
        filteredGradleFiles = []
        for gradleFile in gradleFiles:
            fileReader = FileReader(gradleFile)
            for line in fileReader.getFileLines():
                if dependencyToFilterOn in line:
                    filteredGradleFiles.append(gradleFile)
        return filteredGradleFiles

