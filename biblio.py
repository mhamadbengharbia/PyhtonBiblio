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
