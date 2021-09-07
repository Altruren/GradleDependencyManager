from file.FileUpdater import FileUpdater
from strategies.GradlePropertyBuildStrategy import GradlePropertyBuildStrategy


class GradlePropertiesUpdater:
    def __init__(self, fileName):
        self.fileUpdater = FileUpdater(fileName)

    def updateGradleProperties(self, dependencyToUpdate, newVersion):
        self.fileUpdater.update(GradlePropertyBuildStrategy(dependencyToUpdate, newVersion))