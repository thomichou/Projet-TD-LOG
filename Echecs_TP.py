# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 14:13:59 2015

@author: sajid
"""
import numpy

class Piece:
    
    def __init__(self, position, couleur, valeur):
        self.position = position
        self.valeur = valeur
        self.couleur = couleur

class Pion (Piece):
    
    def __init__(self, position, couleur, valeur):
       Piece.__init__(self, position, couleur, valeur) 
    
    def jouable (self, echiquier):
        i = self.position[0]
        j = self.position[1]
        #cases_possibles = [[i+1, j-1], [i+1, j], [i+1, j+1]]
        cases_valides = []
        if (echiquier.grille[i+1, j] == 0):
            cases_valides.append([i+1, j])
        if (echiquier.grille[i+1, j-1] != 0 and echiquier.grille[i+1, j-1].couleur != self.couleur ):
            cases_valides.append([i+1, j-1])
        if (echiquier.grille[i+1, j+1] != 0 and echiquier.grille[i+1, j+1].couleur != self.couleur ):
            cases_valides.append([i+1, j+1])
        return (cases_valides)
        
class Tour (Piece):
    
    def __init__(self, position, couleur, valeur):
        Piece.__init__(self, position, couleur, valeur) 
    
    def jouable (self, echiquier):
        i = self.position[0]
        j = self.position[1]
        #cases_possibles = [[i+1, j-1], [i+1, j], [i+1, j+1]]
        cases_valides = []
        # limite permet de s arreter dans la ligne ou dans la colonne des que
        # la tour rencontre un obstacle
        limite = 0
        indice = 1
        # on etudie la demi colonne superieure
        while (limite == 0 and indice < 8-i):
            if(echiquier.grille[i+indice, j] == 0):
                cases_valides.append([i+indice, j])
            if(echiquier.grille[i+indice, j] != 0 and echiquier.grille[i+indice, j].couleur != self.couleur):
                cases_valides.append([i+indice, j])
                limite = 1
            else:
                limite = 1
            indice += 1
        # on etudie la demi colonne inferieure
        limite = 0
        indice = 1
        while (limite == 0 and indice < i+1):
            if(echiquier.grille[i-indice, j] == 0):
                cases_valides.append([i-indice, j])
            if(echiquier.grille[i-indice, j] != 0 and echiquier.grille[i-indice, j].couleur != self.couleur):
                cases_valides.append([i-indice, j])
                limite = 1
            else:
                limite = 1
            indice += 1
        # on etudie la semi ligne droite
        limite = 0
        indice = 1
        while (limite == 0 and indice < 8-j):
            if(echiquier.grille[i, j+indice] == 0):
                cases_valides.append([i, j+indice])
            if(echiquier.grille[i, j+indice] != 0 and echiquier.grille[i, j+indice].couleur != self.couleur):
                cases_valides.append([i, j+indice])
                limite = 1
            else:
                limite = 1
            indice += 1
        # on etudie la semi ligne gauche
        limite = 0
        indice = 1
        while (limite == 0 and indice < j+1):
            if(echiquier.grille[i, j-indice] == 0):
                cases_valides.append([i, j-indice])
            if(echiquier.grille[i, j-indice] != 0 and echiquier.grille[i, j-indice].couleur != self.couleur):
                cases_valides.append([i, j-indice])
                limite = 1
            else:
                limite = 1
            indice += 1 
            
        return (cases_valides)

class Fou:   
    
    def __init__(self, position, couleur, valeur):
        Piece.__init__(self, position, couleur, valeur) 
    
    def jouable (self, echiquier):
        i = self.position[0]
        j = self.position[1]
        #cases_possibles = [[i+1, j-1], [i+1, j], [i+1, j+1]]
        cases_valides = []
        indice = 1
        limite = 0
        #demi diagonale sup droite
        while(limite == 0 and i+indice < 8 and j + indice < 8):
            if(echiquier.grille[i+indice, j+indice] == 0):
                cases_valides.append([i+indice, j+indice])
            if(echiquier.grille[i+indice, j+indice].couleur != self.couleur):
                cases_valides.append([i+indice, j+indice])
                limite = 1
            else:
                limite = 1
            indice += 1
        #demi diagonale inf gauche
        indice = 1
        limite = 0
        while(limite == 0 and i-indice > 0 and j - indice > 0):
            if(echiquier.grille[i-indice, j-indice] == 0):
                cases_valides.append([i-indice, j-indice])
            if(echiquier.grille[i-indice, j-indice].couleur != self.couleur):
                cases_valides.append([i-indice, j-indice])
                limite = 1
            else:
                limite = 1   
            indice += 1
        #demi diagonale sup gauche
        indice = 1
        limite = 0
        while(limite == 0 and i-indice > 0 and j + indice < 8):
            if(echiquier.grille[i-indice, j+indice] == 0):
                cases_valides.append([i-indice, j+indice])
            if(echiquier.grille[i-indice, j+indice].couleur != self.couleur):
                cases_valides.append([i-indice, j+indice])
                limite = 1
            else:
                limite = 1
            indice += 1
        #demi diagonale inf droite
        indice = 1
        limite = 0
        while(limite == 0 and i-indice > 0 and j + indice < 8):
            if(echiquier.grille[i-indice, j+indice] == 0):
                cases_valides.append([i-indice, j+indice])
            if(echiquier.grille[i-indice, j+indice].couleur != self.couleur):
                cases_valides.append([i-indice, j+indice])
                limite = 1
            else:
                limite = 1
            indice += 1
            
        return (cases_valides)
        
class Dame (Fou, Tour):
    
    def __init__(self, position, couleur, valeur):
        Piece.__init__(self, position, couleur, valeur) 
    
    def jouable (self, echiquier):
        jouables = Fou.jouable(self, echiquier)
        jouables.extend(Tour.jouable(self, echiquier))
        return (jouables)
        
class Cavalier:
    
    def __init__(self, position, couleur, valeur):
        Piece.__init__(self, position, couleur, valeur)
    
    def jouable (self, echiquier):
        i = self.position[0]
        j = self.position[1]
        #cases_possibles = [[i+1, j-1], [i+1, j], [i+1, j+1]]
        cases_valides = []
        if(echiquier.grille[i+1,j+2] == 0 or echiquier.grille[i+1, j+2].couleur != self.couleur):
            cases_valides.append([i+1, j+2])
        if(echiquier.grille[i-1,j+2] == 0 or echiquier.grille[i-1, j+2].couleur != self.couleur):
            cases_valides.append([i-1, j+2])
        if(echiquier.grille[i-1,j-2] == 0 or echiquier.grille[i-1, j-2].couleur != self.couleur):
            cases_valides.append([i-1, j-2])
        if(echiquier.grille[i+1,j-2] == 0 or echiquier.grille[i+1, j-2].couleur != self.couleur):
            cases_valides.append([i+1, j-2])
        return (cases_valides)

class Roi:
    
    def __init__(self, position, couleur, valeur):
        Piece.__init__(self, position, couleur, valeur)
    
    def jouable (self, echiquier):
        i = self.position[0]
        j = self.position[1]
        #cases_possibles = [[i+1, j-1], [i+1, j], [i+1, j+1]]
        cases_valides = []        
        # il faut verifier si le roi mange une piece qui se trouve dans une des positions 
        # valides d'une autre piece ennemiee
        # rmq notation un peu ambigue. echiquier donne en para designe l objet echiquier
        # et du coup depuis le debut du programme j aurai du ecrire echiquier.echiquier
        if(echiquier.grille[i+1, j] == 0):
            cases_valides.append([i+1, j])
        if(echiquier.grille[i-1, j] == 0):
            cases_valides.append([i-1, j])
        if(echiquier.grille[i, j+1] == 0):
            cases_valides.append([i, j+1])
        if(echiquier.grille[i, j-1] == 0):
            cases_valides.append([i, j-1])
        if(echiquier.grille[i+1, j+1] == 0):
            cases_valides.append([i+1, j+1])
        if(echiquier.grille[i-1, j-1] == 0):
            cases_valides.append([i-1, j-1])
        if(echiquier.grille[i+1, j-1] == 0):
            cases_valides.append([i+1, j-1])
        if(echiquier.grille[i-1, j+1] == 0):
            cases_valides.append([i-1, j+1])
        
        
class Echiquier:
    # compteur permet de savoir c est a qui de joueur, blanc pour 1, -1 pr noir
    compteur = 1 
    P1 = Pion([0,0], blanc, 0)
    
    def __init__(self):
        self.grille = numpy.array([])
    
   # def cases_jouables(self):
   # def deplacement(self):