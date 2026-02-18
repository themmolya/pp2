# Class variables vs instance variables

class University:
    country = "Kazakhstan"   # Class variable

    def __init__(self, name):
        self.name = name     # Instance variable

uni1 = University("NU")
uni2 = University("KBTU")

print(uni1.name, "-", uni1.country)
print(uni2.name, "-", uni2.country)
