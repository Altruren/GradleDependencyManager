from file.FileExtractor import FilePropertyExtractor
from strategies.GradleVersionReadStrategy import GradleVersionStrategy


class VersionRetriever:
    def __init__(self, gradlePropertiesFile):
        self.fileExtractor = FilePropertyExtractor(gradlePropertiesFile)

    def retrieveVersionFromGradleProperties(self):
        return self.fileExtractor.getPropertyFromFile(GradleVersionStrategy("version"))
