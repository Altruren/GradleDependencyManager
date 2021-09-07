from GradleVersionReadStrategy import ReadStrategy


class GradlePropertyReadStrategy(ReadStrategy):

    def __init__(self, property):
        self.property = property

    def extract(self, lines):
        splitter = "="
        for line in lines:
            if self.property in line:
                propertyToRetrieve = self.getProperty(line, splitter)
                return self.getVersion(propertyToRetrieve).strip("\n")

    def getProperty(self, line, splitter):
        return line.split(splitter)[1]

    def getVersion(self, property):
        gradleDependencySplitter = ":"
        versionSplitLocation = 2
        return property.split(gradleDependencySplitter)[versionSplitLocation]