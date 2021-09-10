from strategies.ReadStrategy import ReadStrategy

class GradleVersionReadStrategy(ReadStrategy):

    def __init__(self, version):
        self.version = version

    def extract(self, lines):
        splitter = "="
        for line in lines:
            lineToTest = self.removeWhiteSpaceForComparison(line)
            if lineToTest.startswith(self.version + splitter):
                split = line.split(splitter)
                return split[1].strip("\n")

    def removeWhiteSpaceForComparison(self, string):
        return string.replace(" ", "")
