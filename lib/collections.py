class Collector:
    def __init__(self):
        self.collections = dict()

    def add(self, key, value):
        if key not in self.collections:
            self.collections[key] = []
        collection = self.collections[key]
        collection.append(value)
