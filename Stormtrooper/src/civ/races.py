class Races(object):
    """A given race in the universe

    Attributes:
        affinity: a race's preference of planet type. see: affinity.py
        trait_one: a race's archetype. see: traits.py
        trait_two: a race's archetype. see: traits.py
        industrial_modifier: a race's aptitude for industry. Double between -1.0 and 1.0
        science_modifier: a race's aptitude for science. Double between -1.0 and 1.0
        military_modifier: a race's aptitude for warfare. Double between -1.0 and 1.0
        economic_modifier: a race's aptitude for economy. Double between -1.0 and 1.0

    Methods:
        set_trait_one: incase we need to change a race's first trait.
        set_trait_two: incase we need to change a race's second trait.
        change_industrial_modifier: addittions or subtractions to a race's aptitude for industry.
        change_science_modifier: additions or subtractions to a race's aptitude for science.
        change_military_modifier: additions or subtractions to a race's aptitude for military.
        change_economic_modifier: additions or subtractions to a race's aptitude for economy.
    """
    def __init__(self, name, affinity, trait_one, trait_two, industrial, scientific, militaristic, economic):
        self.name = name
        self.affinity = affinity
        self.trait_one = trait_one
        self.trait_two = trait_two
        self.industrial_modifier = industrial
        self.science_modifier = scientific
        self.military_modifier = militaristic
        self.economic_modifier = economic

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

    def change_economic_modifier(self, economic_change):
        self.economic_modifier = self.economic_modifier + economic_change

    def industrial_values(self):
        self.global_building_cost = (industrial_modifier * -2)

    def scientific_values(self):
        self.research_speed = (science_modifier * 3) + (economic_modifier * 1)
        self.research_building_cost = (science_modifier * -1) + (industrial_modifier * -2) + (economic_modifier * -1)

    def military_values(self):
        self.morale = 1 + (military_modifier * 2)
        self.discipline = 100 + (military_modifier * 10)

    def economic_values(self):
        self.trade_bonus = (economic_modifier * 5)


    #TODO: Define values that will be set based on industrial, science, and military modifiers. 