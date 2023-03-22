# OOO and terminology

# class - a template
# method or message - a defined capability of a class
# field or attribute - a bit of data in a class
# object or instance - a particular instance of a class

# our first class and object

class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)


an = PartyAnimal()

an.party()
an.party()
an.party()

# object lifecycle


class PartyDanimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x += 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)


anobj = PartyDanimal()
anobj.party()
anobj.party()

anobj = 42

print('anobj contains', anobj)


class DartyAnimal():
    x = 0
    name = ""

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x += 1
        print(self.name, "party count", self.x)


# object inheritance


class FootballFan(DartyAnimal):
    points = 0

    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name, "points", self.points)


s = DartyAnimal('Sally')
s.party()

j = FootballFan('Jim')
j.party()
j.touchdown()
