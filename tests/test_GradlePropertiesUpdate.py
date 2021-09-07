import unittest

from FilePropertyExtractor import FilePropertyExtractor
from GradlePropertiesUpdater import GradlePropertiesUpdater
from GradlePropertyReadStrategy import GradlePropertyReadStrategy


class MyTestCase(unittest.TestCase):
    def test_UpdateVersionGradleProperties(self):
        property = "com.example.package:Dependency"
        testGradleProperties = "test-updated-gradle.properties"
        updater = GradlePropertiesUpdater("gradle.properties")
        updater.updateGradleProperties(property, "1.0.1", testGradleProperties)

        filePropertyRetriever = FilePropertyExtractor(testGradleProperties)
        expectedVersion = filePropertyRetriever.getPropertyFromFile(property, GradlePropertyReadStrategy())
        self.assertEqual("1.0.1", expectedVersion)
