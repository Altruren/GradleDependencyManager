from unittest import TestCase
from VersionRetriever import VersionRetriever


class Test(TestCase):
    def test_dependency_is_retrieved_from_gradle_properties(self):
        finder = VersionRetriever()
        version = finder.retrieveVersionFromGradleProperties()
        self.assertEqual(version, "1.0.0")
