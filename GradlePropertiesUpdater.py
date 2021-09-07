from file.FilePropertyUpdater import FilePropertyUpdater
from strategies.GradlePropertyBuildStrategy import GradlePropertyBuildStrategy


class GradlePropertiesUpdater:
    def __init__(self, fileName):
        self.fileUpdater = FilePropertyUpdater(fileName)

    def updateGradleProperties(self, dependencyToUpdate, newVersion):
        self.fileUpdater.update(GradlePropertyBuildStrategy(dependencyToUpdate, newVersion))