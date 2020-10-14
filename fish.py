class Fish:
    def __init__(self,scale,fins,gills,tooth):
        self.scale = scale
        self.fins = fins
        self.gills = gills
        self.tooth = tooth



class Wihte_Shark(Fish):

    def __init__(self,scale,fins,gills,tooth):
        super().__init__(scale,fins,gills,tooth)
        self.size = 6
        self.speed = 56
        self.terrible = True
        self.sharp_tooth = True
        self.very_hungry = True

    def eat(self,food):
        if food > 0:
            print('Акула наелась')
        else:
            print('Акула умерла от голода')


class Blue_Whale(Fish):
    def __init__(self, scale, fins, gills, tooth):
        super().__init__(scale, fins, gills, tooth)
        self.size = 25
        self.blowhole = True
        self.whalebone = True

    def eat(self,food):
        if food > 0:
            print('рост')
        else:
            print('голод')





