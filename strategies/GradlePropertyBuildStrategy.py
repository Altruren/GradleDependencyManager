from datamodel.GradleProperty import GradleProperty
from strategies.BuildStrategy import BuildStrategy


class GradlePropertyBuildStrategy(BuildStrategy):

    def __init__(self, dependencyToUpdate, newVersion):
        self.dependencyToUpdate = dependencyToUpdate
        self.newVersion = newVersion

    def build(self, lines):
        newFileString = ""
        for line in lines:
            lineToAdd = line
            if self.dependencyToUpdate in line:
                lineToAdd = self.buildGradleProperty(line, self.newVersion)
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
