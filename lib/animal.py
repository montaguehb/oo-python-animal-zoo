SPECIES = ["cat", "rat", "dog"]

class Animal:
    all = []
    # def __init__(self, **kwargs):
    #     for key, value in kwargs.items():
    #         setattr(self, f'_{key}', value)
    #     Animal.all.append(self)
    
    def __init__(self, nickname, weight, species, zoo):
        self._nickname = nickname
        self.weight = weight
        if species in SPECIES:
            self._species = species
        else:
            raise AttributeError
        self._zoo = zoo
        
        Animal.all.append(self)
    
    @property    
    def species(self):
        return self._species
    
    @species.setter
    def species(self):
        raise AttributeError
    
    @property    
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, weight):
        if isinstance(weight, int):
            self._weight = weight
        else:
            raise TypeError
    
    @property    
    def nickname(self):
        return self._nickname
    
    @nickname.setter
    def nickname(self):
        raise AttributeError
    
    @property    
    def zoo(self):
        return self._zoo
    
    @zoo.setter
    def zoo(self):
        raise AttributeError
    
    @classmethod
    def find_by_species(cls, species):
        return [animal for animal in cls.all if animal.species == species]
