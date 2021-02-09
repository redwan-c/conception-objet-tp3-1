class Box:
    def __init__(self):
        self._contents = []
    def add(self,truc):
        self._contents.append(truc)        
    def _contains_(self, truc):
        return truc in self._contents
    def remove(self, truc):
        self._contents.remove(truc)  