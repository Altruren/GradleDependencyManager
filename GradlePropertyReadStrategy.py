from GradleVersionReadStrategy import ExtractionStrategy


class GradlePropertyReadStrategy(ExtractionStrategy):
    def extract(self, lines, extractee):
        splitter = "="
        for line in lines:
            if extractee in line:
                property = self.getProperty(line, splitter)
                return self.getVersion(property).strip("\n")

    def getProperty(self, line, splitter):
        return line.split(splitter)[1]

    def getVersion(self, property):
        gradleDependencySplitter = ":"
        versionSplitLocation = 2
        return property.split(gradleDependencySplitter)[versionSplitLocation]