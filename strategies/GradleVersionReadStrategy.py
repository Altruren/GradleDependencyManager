from strategies.ReadStrategy import ReadStrategy


class GradleVersionStrategy(ReadStrategy):
    def extract(self, lines, extractee):
        splitter = "="
        for line in lines:
            if line.startswith(extractee + splitter):
                split = line.split(splitter)
                return split[1].strip("\n")
