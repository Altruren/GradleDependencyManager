class ExtractionStrategy(object):
    def extract(self, lines, extractee):
        pass

class GradleVersionStrategy(ExtractionStrategy):
    def extract(self, lines, extractee):
        splitter = "="
        for line in lines:
            if line.startswith(extractee + splitter):
                split = line.split(splitter)
                return split[1].strip("\n")