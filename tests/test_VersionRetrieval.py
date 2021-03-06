from unittest import TestCase
from VersionRetriever import VersionRetriever


class Test(TestCase):
    def test_dependency_is_retrieved_from_gradle_properties(self):
        finder = VersionRetriever('gradle.properties')
        version = finder.retrieveVersionFromGradleProperties()
        self.assertEqual("1.0.0", version)
