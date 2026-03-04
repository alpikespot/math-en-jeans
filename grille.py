import random as rd
#from numba.experimental import jitclass
import numpy as np
import base64

base64Digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','-','!']

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
    
    def verif_entourage(self, piece):
        self.grille_copy = self.grille.copy()
        self.mettre_dans_grille(piece)
        estBon = True
    
        for x in range(5):
            for y in range(5):
                px = x+piece.x-1
                py = y+piece.y-1

                if (0 <= px <= 5) and (0 <= py <= 5) and self.grille[py][px] <= 0:
                    areanum = self.dfs(px, py)
                    #print(f"area:: {areanum}, verif {px} {py}")
                    #input("conn.")
                    if areanum < 4:
                        estBon = False 
                        break 

        self.grille = self.grille_copy
        return estBon

    def dfs(self, x, y):
        tilenum = 0
        if (0 <= x <= 5) and (0 <= y <= 5) and self.grille[y][x] <= 0:
            self.grille[y][x] = 3
            tilenum += 1

            tilenum += self.dfs(x-1, y)
            tilenum += self.dfs(x, y-1)
            tilenum += self.dfs(x+1, y)
            tilenum += self.dfs(x, y+1)

        return tilenum
    
    def retirer_dernier(self):
        #for i in range(len(self.pieces)):
        #    if self.pieces[i].idx == idx:
        #        rem_piece = self.pieces.pop(i)
        #        break
        rem_piece = self.pieces.pop(-1)
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

    def get_grid_id(self):
        #piece_id[0:9] , flip? , rot[0;4] , posY*6+posX
        idstring = ""
        for piece in self.pieces:
            #compact version
            #idstring += f"{piece.idx}{int(piece.flip)}{piece.rot}{(piece.x+1) * 6 + (piece.y+1)}|"
            
            idstring += f"{piece.idx}{int(piece.flip)}{piece.rot}{piece.x+1}{piece.y+1}|"
            continue
            s = f"{int(piece.flip)+1}{piece.idx}{piece.rot}{piece.x+1}{piece.y+1}"
            val = int(s)
            while val>0:
                idstring += base64Digits[val%(len(base64Digits)-1)]
                val = int(val / val%(len(base64Digits)))
                print(val)
            idstring += "|"

        return idstring
    
    def pieces_manquantes(self):
        piece_manq = [0,1,2,3,4,5,6,7,8]
        #for piece in self.pieces:
        #    print(piece.idx)
        for piece in self.pieces:
            #try: 
                piece_manq.remove(piece.idx)
            #except ValueError:
            #    print(f"VALUE ERROR!!!!!!! ! !!!! {self.pieces}   {piece.idx}")
        return piece_manq
     
    def verif_complete(self):
        for y in range(6):
            for x in range(6):
                if self.grille[y][x] <= 0:
                    return False
        return True
    
    def ajouter(self, piece):
        self.pieces.append(piece)
        self.mettre_dans_grille(piece)
    
    def mettre_dans_grille(self, piece):

        for y in range(3):
            for x in range(3):
                py=y+piece.y;px=x+piece.x

                if piece.piece[y][x] > 0:

                    if self.grille[py][px] <= 0:
                        self.grille[py][px] = piece.piece[y][x]
    


    
        
