import unittest
from animal import Animal
from zoo import Zoo

class Animal_Test(unittest.TestCase):
    name = "New york zoo"
    location = "NY"
    
    def test_animal_species(self):
        zoo = Zoo(name=self.name, location=self.location)
        animal = Animal(species="rat", weight=0, nickname="ratty", zoo=zoo)
        
        with self.assertRaises(Exception):
            Animal(species="Not a rat", weight=1, nickname="Mr boombastic", zoo=zoo)
        self.assertTrue(hasattr(animal, "species"))
        self.assertEqual(animal.species, "rat")
        
    def test_animal_species_immutable(self):
        zoo = Zoo(name=self.name, location=self.location)
        animal = Animal(species="rat", weight=0, nickname="ratty", zoo=zoo)
        
        with self.assertRaises(Exception):
            animal.species = "cat"
            
    def test_animal_nickname(self):
        zoo = Zoo(name=self.name, location=self.location)
        animal = Animal(species="rat", weight=0, nickname="ratty", zoo=zoo)
        
        self.assertTrue(hasattr(animal, "nickname"))
        self.assertEqual(animal.nickname, "ratty")
    
    def test_animal_nickname_immutable(self):
        zoo = Zoo(name=self.name, location=self.location)
        animal = Animal(species="rat", weight=0, nickname="ratty", zoo=zoo)
        
        with self.assertRaises(Exception):
            animal.nickname = "not ratty"
    
    def test_animal_weight(self):
        zoo = Zoo(name=self.name, location=self.location)
        animal = Animal(species="rat", weight=0, nickname="ratty", zoo=zoo)

        self.assertTrue(hasattr(animal, "weight"))
        self.assertEqual(animal.weight, 0)
        animal.weight = 200
        self.assertEqual(animal.weight, 200)
    
    def test_has_all_animals(self):
        zoo = Zoo(name=self.name, location=self.location)
        zoo1 = Zoo(name="Georgia zoo", location="Georgia")
        
        animal = Animal(species="rat", weight=0, nickname="ratty", zoo=zoo)
        animal1 = Animal(species="rat", weight=1, nickname="Mr boombastic", zoo=zoo)
        animal2 = Animal(species="cat", weight=2, nickname="Octavian", zoo=zoo)
        animal3 = Animal(species="dog", weight=3, nickname="Juno", zoo=zoo)
        animal4 = Animal(species="rat", weight=0, nickname="ratty", zoo=zoo1)
        animal5 = Animal(species="cat", weight=1, nickname="mr boombastic", zoo=zoo1)

        self.assertListEqual([animal, animal1, animal2, animal3, animal4, animal5], 
                             Animal.all)
    
    def test_return_zoo(self):
        zoo = Zoo(name=self.name, location=self.location)
        zoo1 = Zoo(name="Georgia zoo", location="Georgia")
        
        animal = Animal(species="rat", weight=0, nickname="ratty", zoo=zoo)
        animal1 = Animal(species="rat", weight=0, nickname="ratty", zoo=zoo1)
        
        self.assertTrue(animal.zoo is zoo)
        self.assertTrue(animal1.zoo is zoo1)
    
    def test_find_by_species(self):
        zoo = Zoo(name=self.name, location=self.location)
        zoo1 = Zoo(name="Georgia zoo", location="Georgia")
        
        animal = Animal(species="rat", weight=0, nickname="ratty", zoo=zoo)
        animal1 = Animal(species="rat", weight=1, nickname="Mr boombastic", zoo=zoo)
        animal3 = Animal(species="dog", weight=3, nickname="Juno", zoo=zoo)
        animal5 = Animal(species="cat", weight=1, nickname="mr boombastic", zoo=zoo1)
        
        self.assertListEqual([animal, animal1], animal.find_by_species("rat"))
        self.assertListEqual([animal3], animal.find_by_species("dog"))
        self.assertListEqual([animal5], animal5.find_by_species("cat"))