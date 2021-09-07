import unittest

from FilePropertyExtractor import FilePropertyExtractor
from FilePropertyUpdater import FilePropertyUpdater
from GradlePropertyStrategy import GradlePropertyStrategy


class MyTestCase(unittest.TestCase):
    def test_UpdateVersionGradleProperties(self):
        property = "com.example.package:Dependency"
        filePropertyUpdater = FilePropertyUpdater("gradle.properties")
        filePropertyUpdater.updateProperty(property, "1.0.1", "test-updated-gradle.properties")

        filePropertyRetriever = FilePropertyExtractor("test-updated-gradle.properties")
        expectedVersion = filePropertyRetriever.getPropertyFromFile(property, GradlePropertyStrategy())
        self.assertEqual("1.0.1", expectedVersion)
