class Voitures():
    prix_litre = 1.70
    def __init__(self,marque="ferrari", modele="sf90", annee=2010, prix = None, couleur = "Blanc", conso = 6.0) :
        self.marque = marque
        self.annee = annee
        self.modele = modele
        self.prix = prix
        self.couleur = couleur
        self.conso = conso



    def __str__(self):
        return f"Valeurs des attributs de l’instance : {self.marque} {self.modele} {self.annee} {self.couleur} {self.conso} {self.prix} "

    def calcul_consommation(self, distance):
        self.distance=distance
        consom=(self.conso/100)*distance
        return f"la {self.modele} fait une distance de {self.distance} km avec une consommation de {consom}L"

    def calcul_prix(self, n):
        self.n=n
        consom=Voitures.calcul_consommation(self,n)
        p = conso * prix_litre
        return f"le prix actuel du carburant {self.n}"




