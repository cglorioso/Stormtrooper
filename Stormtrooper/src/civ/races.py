class Races(object):
    """A given race in the universe

    Attributes:
        affinity: a race's preference of planet type. see: affinity.py
        trait_one: a race's archetype. see: traits.py
        trait_two: a race's archetype. see: traits.py
        industrial_modifier: a race's aptitude for industry. Double between -1.0 and 1.0
        science_modifier: a race's aptitude for science. Double between -1.0 and 1.0
        military_modifier: a race's aptitude for warfare. Double between -1.0 and 1.0

    Methods:
        set_trait_one: incase we need to change a race's first trait.
        set_trait_two: incase we need to change a race's second trait.
        change_industrial_modifier: addittions or subtractions to a race's aptitude for industry.
        change_science_modifier: additions or subtractions to a race's aptitude for science.
        change_military_modifier: additions or subtractions to a race's aptitude for military.
    """
    def __init__(self, name, affinity, trait_one, trait_two, industrial, scientific, militaristic):
        self.name = name
        self.affinity = affinity
        self.trait_one = trait_one
        self.trait_two = trait_two
        self.industrial_modifier = industrial
        self.science_modifier = scientific
        self.military_modifier = militaristic

    def set_trait_one(self, trait):
        self.trait_one = trait

    def set_trait_two(self, trait):
        self.trait_two = trait

    def change_industrial_modifier(self, industrial_change):
        self.industrial_modifier = self.industrial_modifier + industrial_change

    def change_science_modifier(self, science_change):
        self.science_modifier = self.industrial_modifier + science_change

    def change_military_modifier(self, military_change):
        self.military_modifier = self.military_modifier + military_change

    #TODO: Define values that will be set based on industrial, science, and military modifiers. 