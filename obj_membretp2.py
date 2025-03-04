from obj_auteurtp2 import Auteur
from obj_auteurtp2 import Couleur
from obj_livretp2 import Livres

class Membre(Couleur):
    nombre_total_membres=0

    def __init__(self, nom, prenom, date_naissance):
        Membre.nombre_total_membres +=1
        self.id = Membre.nombre_total_membres
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.livres_empruntes = []

    def __str__(self):
        return f"{Livres.BLEU}{self.id}.\t :{Livres.NO_COLOR} {self.prenom} {self.nom} {Membre.MAGENTA}(né(e) le {self.date_naissance})"

    def lister_emprunts(self):
        if len(self.livres_empruntes) ==0 :
            print(f"\t {Membre.ROUGE}'///'{self.prenom} {self.nom} n'a aucun livre emprunté")
        else:
            print(f"{Membre.ROUGE}->\t{Membre.VERT}{self.prenom} {self.nom} a emprunté les livres suivants")
            for i in range(len(self.livres_empruntes)):
                print(f"\t{Membre.BLEU}-{i+1}.{Membre.MAGENTA}\t{self.livres_empruntes[i].titre} de {self.livres_empruntes[i].auteur.prenom} {self.livres_empruntes[i].auteur.nom}")




if __name__ == "__main__":
    print("Création de 2 instances de Membre et affichage...")
    albert = Membre("EINSTEIN", "Albert", "14/03/1879")
    marie = Membre("CURIE", "Marie", "07/11/1867")
    print(albert)
    print(marie)


    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    livre_1 = Livres("Les Piliers de la Terre", follett, "9782130428114", "1989")
    livre_2 = Livres("Une Colonne de Feu", follett, "9782221157695", "2017")
    albert.livres_empruntes.append(livre_1)
    albert.livres_empruntes.append(livre_2)

    albert.lister_emprunts()
    marie.lister_emprunts()



