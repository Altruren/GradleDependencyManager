import unittest

from GradleDependencyFinder import GradleDependencyFinder


class test_FindAllDependencies(unittest.TestCase):
    def test_FindAllGradleFilesWithDependency(self):
        dependencyToFind = "com.example.package:Dependency"
        finder = GradleDependencyFinder("./findAllDependenciesTestDir", dependencyToFind)
        foundGradleFiles = finder.findGradleFilesWithDependency(dependencyToFind)
        foundBuildGradles = foundGradleFiles.count("build.gradle")
        foundGradleProperties = foundGradleFiles.count("gradle.properties")
        self.assertEqual(1, foundBuildGradles)
        self.assertEqual(3, foundGradleProperties)
