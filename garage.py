from obj_voiturestp1 import Voitures

car=Voitures("Renault", "Captur_TCE_90ch", 2018, "20000£", "Gris foncé", 7.21)
print(car)
car2=Voitures("Renault", "Clio-TCE_100ch", 2018, "17000£", "Bleu nuit", 5.51)
print(car2)

consommation=Voitures.calcul_consommation(car2, 1060)
print(consommation)

prix=Voitures.calcul_prix(car, 1060)
print(prix)