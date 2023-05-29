from lib.animal import Animal

class Zoo:
    
    all = []
    
    def __init__(self, name, location=""):
        self.name = name
        self.location = location
        Zoo.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise AttributeError
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if isinstance(location, str):
            self._location = location
        else:
            raise AttributeError