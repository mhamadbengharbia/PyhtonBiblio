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
