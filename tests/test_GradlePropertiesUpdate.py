import unittest

from file.FilePropertyExtractor import FilePropertyExtractor
from GradlePropertiesUpdater import GradlePropertiesUpdater
from strategies.GradlePropertyReadStrategy import GradlePropertyReadStrategy


class MyTestCase(unittest.TestCase):
    def test_UpdateVersionGradleProperties(self):
        property = "com.example.package:Dependency"
        testGradleProperties = "gradle.properties"
        updater = GradlePropertiesUpdater(testGradleProperties)
        updater.updateGradleProperties(property, "1.0.2")
        self.assertEqual("1.0.2", self.getVersionFromGradleProperties(property, testGradleProperties))
        updater.updateGradleProperties(property, "1.0.1")
        self.assertEqual("1.0.1", self.getVersionFromGradleProperties(property, testGradleProperties))

    def getVersionFromGradleProperties(self, property, testGradleProperties):
        filePropertyRetriever = FilePropertyExtractor(testGradleProperties)
        return filePropertyRetriever.getPropertyFromFile(property, GradlePropertyReadStrategy())
