import unittest

from GradleDependencyFinder import GradleDependencyFinder


class test_FindAllDependencies(unittest.TestCase):
    def test_FindAllGradleFilesWithDependencies(self):
        dependencyToFind = "com.example.package:Dependency"
        finder = GradleDependencyFinder(".", dependencyToFind)
        foundGradleFiles = finder.findGradleFilesWithDependency(dependencyToFind)
        foundBuildGradles = foundGradleFiles.count("build.gradle")
        foundGradleProperties = foundGradleFiles.count("gradle.properties")
        self.assertEqual(2, foundBuildGradles)
        self.assertEqual(3, foundGradleProperties)
