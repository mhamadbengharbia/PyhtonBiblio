class Livre:
    def __init__(self , titre , auteur , prix , nbpages):
        self.titre = titre
        self.auteur = auteur
        self.prix = prix
        self.nbpages = nbpages
        self.proprietaire = None
        
    def __str__(self):
        if self.proprietaire == None:
            res = " // Livre neuf"
        else:
            res = "  // Propriétaire : " + self.proprietaire
            
        return "Titre : " + self.titre + "  // Auteur : " + self.auteur + " // Prix : " + str(self.prix) + " // Propriétaire : " + res
    
    def acheter(self , proprietaire):
        if self.proprietaire == None:
            self.proprietaire = proprietaire
        else :
            print("Livre déjà vendu")
class BD:
    def __init__(self , titre , auteur , prix , nbpages , enCouleur):
        self.titre = titre
        self.auteur = auteur
        self.prix = prix
        self.nbpages = nbpages
        self.proprietaire = None
        self.enCouleur = enCouleur
        
    def __str__(self):
        if self.proprietaire == None:
            res = " // Livre neuf"
        else:
            res = "  // Propriétaire : " + self.proprietaire
            
        return "Titre : " + self.titre + "  // Auteur : " + self.auteur + " // Prix : " + str(self.prix) + " // Propriétaire : " + res
    
    def acheter(self , proprietaire):
        if self.proprietaire == None:
            self.proprietaire = proprietaire
        else :
            print("Livre déjà vendu")
            
            
    def echanger(self , bd2):
        if self.proprietaire == None or bd2.proprietaire == None :
            print("Echange impossible, l'une des BD est neuve")
        else :
            if self.prix != bd2.prix :
                print("Echange impossible, le prix n'est pas le même")
            else:
                temp = self.proprietaire
                self.proprietaire = bd2.proprietaire
                bd2.proprietaire = temp
class BibDeClasse:
    def __init__(self):
        self.bibliotheque = []
    
    def ajouter(self, oeuvre):
        if oeuvre not in self.bibliotheque:
            self.bibliotheque.append(oeuvre)
        else :
            print("L'oeuvre existe déjà")
    
    def supprimer(self, oeuvre):
        if oeuvre in self.bibliotheque:
            self.bibliotheque.remove(oeuvre)
        else :
            print("L'oeuvre n'existe pas")
            
    def afficher(self):
        for x in self.bibliotheque :
           print(x)  
hp = Livre("Harry Potter", "J. K. Rowling", 79.9, 350)
print(hp)
print()
hp.acheter("Hatem")
hp.acheter("Fatma")
print(hp)
print()
tintin1 = BD("Tintin en Amérique", "Hergé", 40.0, 80, enCouleur=True)
tintin2 = BD("Tintin au Congo", "Hergé", 40.0, 80, enCouleur=True)
tintin1.echanger(tintin2)
print()
print(tintin2)
print()
bibrsi2 = BibDeClasse()
bibrsi2.ajouter(tintin1)
bibrsi2.ajouter(tintin2)
bibrsi2.ajouter(hp)
bibrsi2.ajouter(tintin1)
bibrsi2.supprimer(tintin1)
bibrsi2.supprimer(tintin1)
bibrsi2.ajouter(tintin1)
print()
bibrsi2.afficher()
