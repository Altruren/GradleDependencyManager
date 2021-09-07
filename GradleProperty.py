class GradleProperty:
    def __init__(self, propertyName, module, group, version):
        self.propertyName = propertyName
        self.module = module
        self.group = group
        self.version = version
        self.propertySeparator = "="
        self.dependencySeparator = ":"

    def __str__(self):
        return self.propertyName + \
               self.propertySeparator + \
               self.module + \
               self.dependencySeparator + \
               self.group + \
               self.dependencySeparator + \
               self.version + "\n"