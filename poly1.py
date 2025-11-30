class Animal:
    def parler(self):
        raise NotImplementedError("Cette méthode doit être redéfinie")

class Chien(Animal):
    def parler(self):
        return "Ouaf !"

class Chat(Animal):
    def parler(self):
        return "Miaou !"

class Vache(Animal):
    def parler(self):
        return "Meuh !"

# Exemple de duck typing
class Robot:
    def parler(self):
        return "Bip bip !"

def faire_parler(animal):
    print(animal.parler())

if __name__ == "__main__":
    animaux = [Chien(), Chat(), Vache(), Robot()]
    for a in animaux:
        faire_parler(a)
