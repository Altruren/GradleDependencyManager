import unittest

from file.FilePropertyExtractor import FilePropertyExtractor
from GradlePropertiesUpdater import GradlePropertiesUpdater
from strategies.GradlePropertyReadStrategy import GradlePropertyReadStrategy


class MyTestCase(unittest.TestCase):
    def test_UpdateVersionGradleProperties(self):
        property = "com.example.package:Dependency"
        testGradleProperties = "gradle.properties"
        updater = GradlePropertiesUpdater(testGradleProperties)
        updater.updateGradleProperties(property, "1.0.1")

        filePropertyRetriever = FilePropertyExtractor(testGradleProperties)
        expectedVersion = filePropertyRetriever.getPropertyFromFile(property, GradlePropertyReadStrategy())
        self.assertEqual("1.0.1", expectedVersion)
