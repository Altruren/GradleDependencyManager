from file.FileExtractor import FilePropertyExtractor
from strategies.GradleVersionReadStrategy import GradleVersionReadStrategy


class VersionRetriever:
    def __init__(self, gradlePropertiesFile):
        self.fileExtractor = FilePropertyExtractor(gradlePropertiesFile)

    def retrieveVersionFromGradleProperties(self):
        return self.fileExtractor.getPropertyFromFile(GradleVersionReadStrategy("version"))
