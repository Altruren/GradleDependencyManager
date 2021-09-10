class GradleVersionProperty:
    def __init__(self, propertyName, propertyDefinition):
        self.propertyName = propertyName
        self.propertyDefinition = propertyDefinition
        self.propertySeparator = "="

    def __str__(self):
        return self.propertyName + self.propertySeparator + self.propertyDefinition + "\n"
