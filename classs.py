class Planet:
    """Этот класс"""

    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return f'Планета: {self.name}!'
list_of_planet = ['Earth','Mars','Mercury','Venus','Saturn','Pluton','Jupiter''Neptun']
solary_sistem = []
for planet in list_of_planet:
    new_planet = Planet(planet)
    solary_sistem.append(new_planet)
print(solary_sistem)