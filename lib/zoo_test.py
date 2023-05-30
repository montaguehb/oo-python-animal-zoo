import unittest
from animal import Animal
from zoo import Zoo

class Zoo_Test(unittest.TestCase):
    name = "New york zoo"
    location = "NY"
    
    def test_has_name(self):
        Zoo.all = []
        Animal.all = []
        zoo = Zoo(name=self.name)
        self.assertTrue(hasattr(zoo, "name"), "Zoo does not have a name attribute")
        self.assertEqual(zoo.name, self.name, "Name is not equal to New york zoo")
    
    def test_has_location(self):
        Zoo.all = []
        Animal.all = []
        
        zoo = Zoo(name="New york zoo", location=self.location)
        self.assertTrue(hasattr(zoo, "location"), "Zoo does not have a location attribute")
        self.assertEqual(zoo.location, self.location, "Location is not equal to NY")
    
    def test_name_is_string(self):
        Zoo.all = []
        Animal.all = []
        with self.assertRaises(Exception):
            Zoo(name=3, location=self.location)
        zoo = Zoo(name=self.name, location=self.location)
        self.assertIsInstance(zoo.name, str)
        
    def test_location_is_string(self):
        Zoo.all = []
        Animal.all = []
        with self.assertRaises(Exception):
            Zoo(name=self.name, location=3)
        zoo = Zoo(name=self.name, location=self.location)
        self.assertIsInstance(zoo.location, str)    
        
    def test_zoo_has_all(self):
        Zoo.all = []
        Animal.all = []
        name1 = "Georgia Zoo"
        location1 = "Georgia"
        zoo = Zoo(name="New york zoo", location=self.location)
        zoo1 = Zoo(name=name1, location=location1)
        self.assertTrue(hasattr(Zoo, "all"), "Zoo does not contain an all attribute")
        self.assertTrue(zoo in Zoo.all and zoo1 in Zoo.all, "Zoo does not contain all zoes")
    
    def test_zoo_has_animals(self):
        Zoo.all = []
        Animal.all = []
        
        zoo = Zoo(name=self.name, location=self.location)
        zoo1 = Zoo(name="Georgia zoo", location="Georgia")
        
        animal = Animal(species="rat", weight=0, nickname="ratty", zoo=zoo)
        animal1 = Animal(species="rat", weight=1, nickname="Mr boombastic", zoo=zoo)
        animal2 = Animal(species="cat", weight=2, nickname="Octavian", zoo=zoo)
        animal3 = Animal(species="dog", weight=3, nickname="Juno", zoo=zoo)
        animal4 = Animal(species="rat", weight=0, nickname="ratty", zoo=zoo1)
        animal5 = Animal(species="rat", weight=1, nickname="mr boombastic", zoo=zoo1)
        
        self.assertCountEqual([animal, animal1, animal2, animal3],zoo.animals())
        self.assertCountEqual([animal4, animal5],zoo1.animals())
    
    def test_zoo_animal_species(self):
        Zoo.all = []
        Animal.all = []
        
        zoo = Zoo(name=self.name, location=self.location)
        zoo1 = Zoo(name="Georgia zoo", location="Georgia")
        
        Animal(species="rat", weight=0, nickname="ratty", zoo=zoo)
        Animal(species="rat", weight=1, nickname="Mr boombastic", zoo=zoo)
        Animal(species="cat", weight=2, nickname="Octavian", zoo=zoo)
        Animal(species="dog", weight=3, nickname="Juno", zoo=zoo)
        Animal(species="rat", weight=0, nickname="ratty", zoo=zoo1)
        Animal(species="cat", weight=1, nickname="mr boombastic", zoo=zoo1)

        self.assertSetEqual({"cat", "rat", "dog"}, zoo.animal_species())
        self.assertSetEqual({"cat", "rat"}, zoo1.animal_species())
        
    def test_find_by_species(self):
        Zoo.all = []
        Animal.all = []
        
        zoo = Zoo(name=self.name, location=self.location)
        zoo1 = Zoo(name="Georgia zoo", location="Georgia")
        
        animal = Animal(species="rat", weight=0, nickname="ratty", zoo=zoo)
        animal1 = Animal(species="rat", weight=1, nickname="Mr boombastic", zoo=zoo)
        animal3 = Animal(species="dog", weight=3, nickname="Juno", zoo=zoo)
        animal5 = Animal(species="cat", weight=1, nickname="mr boombastic", zoo=zoo1)
        
        self.assertCountEqual([animal, animal1], zoo.find_by_species("rat"))
        self.assertCountEqual([animal3], zoo.find_by_species("dog"))
        self.assertCountEqual([animal5], zoo1.find_by_species("cat"))
    
    def test_has_animal_nicknames(self):
        Zoo.all = []
        Animal.all = []
        zoo = Zoo(name=self.name, location=self.location)
        zoo1 = Zoo(name="Georgia zoo", location="Georgia")
        
        animal = Animal(species="rat", weight=0, nickname="ratty", zoo=zoo)
        animal1 = Animal(species="rat", weight=1, nickname="Mr boombastic", zoo=zoo)
        animal2 = Animal(species="cat", weight=2, nickname="Octavian", zoo=zoo)
        animal3 = Animal(species="dog", weight=3, nickname="Juno", zoo=zoo)
        animal4 = Animal(species="rat", weight=0, nickname="ratty", zoo=zoo1)
        animal5 = Animal(species="cat", weight=1, nickname="mr boombastic", zoo=zoo1)
        
        self.assertCountEqual(
            [animal1.nickname, animal.nickname, animal2.nickname, animal3.nickname],
            zoo.animal_nicknames()
            )
        
        self.assertCountEqual(
            [animal4.nickname, animal5.nickname],
            zoo1.animal_nicknames()
        )
    
    def test_find_by_location(self):
        Zoo.all = []
        Animal.all = []
        zoo = Zoo(name=self.name, location=self.location)
        zoo1 = Zoo(name=self.name, location=self.location)
        zoo2 = Zoo(name=self.name, location=self.location)
        zoo3 = Zoo(name="Georgia zoo", location="Georgia")
        zoo4 = Zoo(name="Georgia zoo", location="Georgia")
        
        self.assertCountEqual([zoo, zoo1, zoo2], Zoo.find_by_location("NY"))
        self.assertCountEqual([zoo3, zoo4], Zoo.find_by_location("Georgia"))