from strategies.ReadStrategy import ReadStrategy


class GradleVersionStrategy(ReadStrategy):

    def __init__(self, version):
        self.version = version

    def extract(self, lines):
        splitter = "="
        for line in lines:
            if line.startswith(self.version + splitter):
                split = line.split(splitter)
                return split[1].strip("\n")
