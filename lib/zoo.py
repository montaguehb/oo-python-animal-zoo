from animal import Animal

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
    
    def animals(self):
        return [animal for animal in Animal.all if animal.zoo is self]
    
    def animal_species(self):
        species = set()
        for animal in Animal.all:
            if animal.species in species or animal.zoo is not self:
                continue
            species.add(animal.species)
             
        return species
    
    def find_by_species(self, species):
        return [animal for animal in Animal.all if animal.species == species]
    
    def animal_nicknames(self):
        return [animal.nickname for animal in Animal.all if animal.zoo is self]
    
    @classmethod
    def find_by_location(cls, location):
        return [zoo for zoo in cls.all if zoo.location == location]