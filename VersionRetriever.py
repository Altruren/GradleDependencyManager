from FilePropertyExtractor import FilePropertyExtractor
from GradleVersionStrategy import GradleVersionStrategy


class VersionRetriever:
    def __init__(self, gradlePropertiesFile):
        self.fileExtractor = FilePropertyExtractor(gradlePropertiesFile)

    def retrieveVersionFromGradleProperties(self):
        return self.fileExtractor.getPropertyFromFile("version", GradleVersionStrategy())
