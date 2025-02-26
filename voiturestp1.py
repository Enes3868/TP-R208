class Voitures():
    def __init__(self,marque="ferrari", modele="sf90", annee=2010) :
        self.marque = marque
        self.annee = annee
        self.modele = modele



    def __str__(self):
        return f"Valeurs des attributs de l’instance : {self.marque} {self.modele} {self.annee}"
car = Voitures("Renault", "Clio", 2018)
caisse = car.modele
print(f"J’ai une {car.marque} {caisse} de {car.annee} !")
car.annee = 2020
print(f"J’ai une {car.marque} {caisse} de {car.annee} !")
print(car)
car2 = Voitures("Bugatti", "Veyron")
print(car2)
car3 = Voitures()
print(car3)
car4 = Voitures("F40")
print(car4)
voiture6 = Voitures(modele = "296_GTS")
print(voiture6)

print(type(voiture6))
print(vars(voiture6))
print(dir(voiture6))




