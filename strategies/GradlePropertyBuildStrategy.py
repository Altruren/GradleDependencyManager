from datamodel.GradleProperty import GradleProperty
from datamodel.GradleVersionProperty import GradleVersionProperty
from strategies.BuildStrategy import BuildStrategy


class GradlePropertyBuildStrategy(BuildStrategy):

    def __init__(self, dependencyToUpdate, newVersion):
        self.dependencyToUpdate = dependencyToUpdate
        self.newVersion = newVersion
        self.propertySeparator = "="
        self.dependencySeparator = ":"

    def build(self, lines):
        newFileString = ""
        for line in lines:
            lineToAdd = line
            if self.isDependencyInLine(line):
                if (self.isFullDependencyFormat(line)):
                    lineToAdd = self.buildGradleFullDependency(line, self.newVersion)
                else:
                    lineToAdd = self.buildGradleVersionProperty(line, self.newVersion)
            newFileString += lineToAdd
        return newFileString

    def isFullDependencyFormat(self, line):
        colonsInDependencyFormat = 2
        return line.count(":") == colonsInDependencyFormat

    def isDependencyInLine(self, line):
        return self.dependencyToUpdate in line

    def buildGradleFullDependency(self, line, newVersion):
        propertySplit = line.split(self.propertySeparator)
        propertyName = propertySplit[0]
        propertyDefinition = propertySplit[1]
        dependencySplit = propertyDefinition.split(self.dependencySeparator)
        module = dependencySplit[0]
        group = dependencySplit[1]

        gradleProperty = GradleProperty(propertyName, module, group, newVersion)

        return str(gradleProperty)

    def buildGradleVersionProperty(self, line, newVersion):
        propertySplit = line.split(self.propertySeparator)
        propertyName = propertySplit[0]

        gradleVersionProperty = GradleVersionProperty(propertyName, newVersion)
        return str(gradleVersionProperty)
