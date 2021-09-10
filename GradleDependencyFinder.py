import os

from file.FileFilterer import FileFilterer
from file.FileReader import FileReader
from os.path import isdir
from os.path import join


class GradleDependencyFinder:
    def __init__(self, parentDirectory, dependencyToFind):
        self.parentDirectory = parentDirectory
        self.dependencyToFind = dependencyToFind

    def findGradleFilesWithDependency(self, dependency):
        gradleFiles = self.findAllGradleFiles(self.parentDirectory)
        return self.filterGradleFilesThatHaveDependency(gradleFiles, dependency)

    def findAllGradleFiles(self, directory):
        fileList = os.listdir(directory)
        gradleFiles = FileFilterer().filterFilesWithValidName(fileList)
        for subElement in fileList:
            fullPath = join(directory, subElement)
            if isdir(fullPath):
                gradleFiles.extend(self.findAllGradleFiles(fullPath))
        return gradleFiles

    def filterGradleFilesThatHaveDependency(self, gradleFiles, dependencyToFilterOn):
        filteredGradleFiles = []
        for gradleFile in gradleFiles:
            fileReader = FileReader(gradleFile)
            for line in fileReader.getFileLines():
                if dependencyToFilterOn in line:
                    filteredGradleFiles.append(gradleFile)
        return filteredGradleFiles

