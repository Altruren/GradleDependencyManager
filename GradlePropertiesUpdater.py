from FilePropertyUpdater import FilePropertyUpdater
from GradlePropertyBuildStrategy import GradlePropertyBuildStrategy


class GradlePropertiesUpdater:
    def __init__(self, fileName):
        self.fileUpdater = FilePropertyUpdater(fileName)

    def updateGradleProperties(self, dependencyToUpdate, newVersion, newFileName):
        self.fileUpdater.updateProperty(GradlePropertyBuildStrategy(dependencyToUpdate, newVersion), newFileName)