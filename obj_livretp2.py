from obj_auteurtp2 import Auteur
from obj_auteurtp2 import Couleur

class Livres(Couleur):
    nombre_total_livres=0

    def __init__(self, titre, auteur, isbn = None, annee_publication = None):
        Livres.nombre_total_livres += 1
        self.id=Livres.nombre_total_livres
        self.titre=titre
        self.auteur=auteur
        self.isbn=isbn if isbn else "N/A"
        self.annee_publication=annee_publication if annee_publication else "N/A"
        self.disponible=True

    def __str__(self):
        return f"{Livres.BLEU}{self.id}.\t :{Livres.NO_COLOR}'{self.titre}' de {self.auteur.prenom} {self.auteur.nom} {Livres.MAGENTA} (ISBN: {self.isbn}, publié en {self.annee_publication}){Livres.NO_COLOR} - {Livres.VERT if self.disponible else Livres.ROUGE} {'Dispo' if self.disponible else 'NON Dispo'}{Livres.NO_COLOR}"


if __name__ == "__main__":
    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    verne = Auteur("VERNE","Jules","France", "08/02/1828")
    print("Création de 3 instances de Livre et affichage...")
    livre_1 = Livres("Les Piliers de la Terre", follett, "9782130428114", "1989")
    livre_2 = Livres("Une Colonne de Feu", follett, "9782221157695", "2017")
    livre_2.disponible = False
    livre_3 = Livres("Vingt Mille Lieues sous les mers", verne, "9782070364234", "1870")
    print(livre_1)
    print(livre_2)
    print(livre_3)




