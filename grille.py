import random as rd
from numba.experimental import jitclass
import numpy as np
class Grille():
    def __init__(self, gr):
        self.grille = gr
        self.grille_originale = np.copy(gr)
        self.pieces = []
        self.nbGrillesPossibles = 0

    def verif_smileys(self, piece):
        for y in range(3):
            for x in range(3):
                posx = x+piece.x ; posy = y+piece.y
                if 0<=posx<=5 and 0<=posy<=5:
                    if piece.piece[y][x] >=1:
                        if self.grille_originale[posy][posx] == -1 and piece.piece[y][x] != 2:
                            #input(f"wrong!! valgrille:{self.grille_originale[posy][posx]}, valpiece:{piece.piece[y][x]}")
                            return False
                        if piece.piece[y][x] == 2 and self.grille_originale[posy][posx] ==0:
                            #input(f"wrong!! valgrille:{self.grille_originale[posy][posx]}, valpiece:{piece.piece[y][x]}")
                            return False
                    #if piece.piece[posy][posx] == 2:
                    #elif piece.piece[posy][posx] == 1:
            
        return True
    
    def verif_trou(self, grille_aux, x, y):
        estTrou = True
        for yy in range(3):
            for xx in range(3):
                if estTrou and not (xx == 1 and yy == 1):
                    if 0<=(yy+y-1)<=5 and 0<=(xx+x-1)<=5 and (yy==1 or xx==1):
                        if grille_aux[yy+y-1][xx+x-1] <= 0:
                            estTrou = False #on a une case vide
        #if not estTrou:
        #    grille_aux[y][x] = 1
        return estTrou
    
    def retirer_dernier(self, idx):
        for i in range(len(self.pieces)):
            if self.pieces[i].idx == idx:
                rem_piece = self.pieces.pop(i)
                break
        for y in range(3):
            for x in range(3):
                posx = rem_piece.x + x 
                posy = rem_piece.y + y 
                if 0<=posx<=5 and 0<=posy<=5 and rem_piece.piece[y][x] >= 1:
                    self.grille[posy][posx] = self.grille_originale[posy][posx]

    def afficher(self, g=None):
        if g == None:
            g = self.grille
        #print(self.pieces_manquantes())
        #print("------------------------------------------------------\nGRILLE:")
        for y in range(6):
            s = ""
            for x in range(6):
                if g[y][x] >=1:
                    s += "# "
                else:
                    s += "- "
            print("|" + s + "|")
        return
        print("PIECES: ")
        for p in self.pieces:
            print(p)
            for y in range(3):
                for x in range(3):
                    if p.piece[y][x] != 0:
                        print(" # ", end=" - ")
                    else:
                        print(" - ", end =" - ")
                print("")
        print("------------------------------------------------------")

                
    def pieces_manquantes(self):
        piece_manq = [0,1,2,3,4,5,6,7,8]
        #for piece in self.pieces:
        #    print(piece.idx)
        for piece in self.pieces:
            piece_manq.remove(piece.idx)
        return piece_manq
     
    def verif_complete(self):
        for y in range(6):
            for x in range(6):
                if self.grille[y][x] <= 0:
                    return False
        return True
    
    def ajouter(self, piece):
        self.pieces.append(piece)
        #self.mettre_dans_grille(piece)
    

    
        
