from FileExtractor import FileExtractor


class VersionRetriever:
    def __init__(self):
        self.fileExtractor = FileExtractor(
            'C:\Users\djohn\AndroidStudioProjects\TestProjectForGradleProperties\gradle.properties')

    def retrieveVersionFromGradleProperties(self):
        versionID = "version="
        splitter = "="
        return self.fileExtractor.getItemFromFile(versionID, splitter)
