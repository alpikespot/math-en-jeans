import random as rd
from copy import deepcopy
class Grille():

    def __init__(self):
        self.grille = self.creer_grille()
        self.pieces = []

    def creer_grille(self):
        grille = []
        for y in range(6):
            gLigne = []
            for x in range(6):
                gLigne.append(0)
            
            grille.append(gLigne)

        #mettre 10 smileys, mais pour le moment je ne m'interesse pas aux smileys
        
        for _ in range(0):
            randX = rd.randrange(6) ; randY = rd.randrange(6) 
            
            while grille[randY][randX] == 1:
                randX = rd.randrange(6) ; randY = rd.randrange(6)
            grille[randY][randX] = -1
        return grille
    
    def afficher(self, g=None):
        if g == None:
            g = self.grille
        #print(self.pieces_manquantes())
        #print("------------------------------------------------------\nGRILLE:")
        for y in range(6):
            s = ""
            for x in range(6):
                if g[y][x]:
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
        self.grille = self.mettre_dans_grille(piece)
    
    def verif_trous(self, piece):
        grille = self.mettre_dans_grille(piece)
        self.afficher(grille)
        print("FONCTION TROUSSS ---- \n FONC TROUSS!a!!!!")
        for y in range(6):
            for x in range(6):
                if grille[y][x] <= 0: #si la case est vide
                    estRemplie = True
                    for yy in range(3):
                        for xx in range(3):
                            if not estRemplie and not (xx == 1 and yy == 1):
                                if 0<=(yy+y-1)<=5 and 0<=(xx+x-1)<=5:
                                    if grille[yy+y-1][xx+x-1] <= 0:
                                        estRemplie = False #on a une case vide
                            
                    if estRemplie:
                        print(f"YA UN TROU A Y:{y} X:{x}!!")
                        return True
        print("PAS DE TROUS,, CONTINUE")
        return False

    def mettre_dans_grille(self, piece):
        grille_ret = deepcopy(self.grille)
        for y in range(3):
            for x in range(3):
                valPiece = piece.piece[y][x]
                if valPiece > 0:
                    valGrille = grille_ret[y+piece.y][x+piece.x]

                    if valGrille == 0:
                        grille_ret[y+piece.y][x+piece.x] = valPiece
        return grille_ret
        
