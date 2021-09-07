import unittest

from GradleDependencyFinder import GradleDependencyFinder


class MyTestCase(unittest.TestCase):
    def test_FindAllGradleFilesWithDependencies(self):
        dependencyToFind = "com.example.package:Dependency"
        finder = GradleDependencyFinder(".", dependencyToFind)
        foundGradleFiles = finder.findGradleFilesWithDependency(dependencyToFind)
        self.assertEqual(foundGradleFiles, ["build.gradle", "gradle.properties"])
