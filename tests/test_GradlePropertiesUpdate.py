import unittest

from file.FileExtractor import FilePropertyExtractor
from GradlePropertiesUpdater import GradlePropertiesUpdater
from strategies.GradlePropertyReadStrategy import GradlePropertyReadStrategy
from strategies.GradleVersionReadStrategy import GradleVersionReadStrategy



class MyTestCase(unittest.TestCase):
    def test_UpdateVersionGradleProperties(self):
        property = "com.example.package:Dependency"
        testGradleProperties = "gradle.properties"
        updater = GradlePropertiesUpdater(testGradleProperties)
        updater.updateGradleProperties(property, "1.0.2")
        self.assertEqual("1.0.2", self.getVersionFromDependencyFormat(property, testGradleProperties))
        updater.updateGradleProperties(property, "1.0.1")
        self.assertEqual("1.0.1", self.getVersionFromDependencyFormat(property, testGradleProperties))

    def test_UpdateVersionPropertyGradleProperties(self):
        property = "dependencyVersion"
        testGradleProperties = "gradle.properties"
        updater = GradlePropertiesUpdater(testGradleProperties)
        updater.updateGradleProperties(property, "3.0.1")
        self.assertEqual("3.0.1", self.getVersionFromVersionFormat(property, testGradleProperties))
        updater.updateGradleProperties(property, "3.0.0")
        self.assertEqual("3.0.0", self.getVersionFromVersionFormat(property, testGradleProperties))

    def getVersionFromDependencyFormat(self, property, testGradleFile):
        filePropertyRetriever = FilePropertyExtractor(testGradleFile)
        return filePropertyRetriever.getPropertyFromFile(GradlePropertyReadStrategy(property))

    def getVersionFromVersionFormat(self, property, testGradleFile):
        filePropertyRetriever = FilePropertyExtractor(testGradleFile)
        return filePropertyRetriever.getPropertyFromFile(GradleVersionReadStrategy(property))

    def test_UpdateVersionWithVariable(self):
        property = "com.example.package:Dependency"
        # testBuildGradle = "build.gradle"
        # testGradleProperties = "gradle.properties"
        # expectedPropertyToUpdate = "dependencyVersion"
        # updater = GradlePropertiesUpdater(testBuildGradle)
        # updater.updateGradleProperties(property, "3.0.0")
        #
        # updatedVersion = self.getVersionFromGradleProperties(expectedPropertyToUpdate, testGradleProperties)
        # self.assertEqual("3.0.0", updatedVersion)




