class ModOfTwo:
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.n=0
        return self
    