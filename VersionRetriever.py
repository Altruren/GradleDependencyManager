from FileExtractor import FileExtractor
from GradleVersionStrategy import GradleVersionStrategy


class VersionRetriever:
    def __init__(self, gradlePropertiesFile):
        self.fileExtractor = FileExtractor(gradlePropertiesFile, GradleVersionStrategy())

    def retrieveVersionFromGradleProperties(self):
        return self.fileExtractor.getPropertyFromFile("version")
