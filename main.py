"""
-commencer avec les pièces à 2 trous

"""
import pygame

from pieces import Pieces
from file import stuff
from grille import Grille
import numpy as np
from numba import njit
import time
pygame.init()
win = pygame.display.set_mode((370, 370))
pygame.display.set_caption("Puzzle grille application")
clock = pygame.time.Clock()

grille1 = np.array([
[0, 0, 0, 0,-1, 0],
[-1,0,-1, 0, 0,-1],
[0, 0, 0,-1, 0, 0],
[0,-1, 0, 0, 0,-1],
[0, 0,-1, 0, 0, 0],
[-1,0, 0,0, 0,-1]], dtype=int)

pieces_grille = []



grille = np.copy(grille1)
print("program begin")
running = True
piecePosX = 0; piecePosY = 0 ; rot = 0
pieceChoisie = 0
p_choisie = None
caseTaille = 50 
ecartCase = 60
pieceIdx = 0

def get_input():
    keys = pygame.key.get_pressed()
    
    

def update_game(pieces):
    #get_input()
    win.fill(pygame.Color(0,0,0,255))
    gr = Grille(np.copy(grille1))
    for y in range(6):
        for x in range(6):
            valCase = grille[y][x]
            
            clr = (200,200,200,255)
            #if valCase == -1:
            #    clr = (150,150,50,255)
            pygame.draw.rect(win, clr, (10 + x*ecartCase, 10 + y*ecartCase, caseTaille, caseTaille))
            if valCase==-1:
                coul= (200, 200,50,255)
            else:
                coul= (200,200,200,255)
            pygame.draw.rect(win, coul, (15 + x * ecartCase + ecartCase/8 
                                            ,15 + y * ecartCase + ecartCase/8 , 
                                            (caseTaille-10)/1.5, 
                                            (caseTaille-10)/1.5))
            #if valCase == 1:
            #    pygame.draw.circle(win, (230,230,0,255), (10 + x*ecartCase + caseTaille/2, 10 + y*ecartCase + caseTaille/2), caseTaille/3)
    
    for piece in pieces:
        piece.dessiner(win, gr)
        
    pygame.display.flip()
    clock.tick(10)

@njit
def verif_smileys_njit(grille_originale, piece, px, py):
    for y in range(3):
        for x in range(3):
            posx = x+px ; posy = y+py
            if 0<=posx<=5 and 0<=posy<=5:
                if piece[y][x] >=1:
                    if grille_originale[posy][posx] == -1 and piece[y][x] != 2:
                        return False
                    if piece[y][x] == 2 and grille_originale[posy][posx] ==0:
                        return False
        
    return True

@njit
def verifier_njit(grille, piece, px, py):
        for y in range(3):
            for x in range(3):
                if piece[y][x] <= 0:
                    continue
                else:
                    if (not 0<=(y+py)<=5 or not (0<=(x+px)<=5)) or grille[y+py][x+px] > 0:
                        #print("piece out of bounds")
                        return False
        return True

@njit
def mettre_dans_grille_njit(piece, pix, piy, grille):

    for y in range(3):
        for x in range(3):
            py=y+piy;px=x+pix

            if piece[y][x] > 0:

                if grille[py][px] <= 0:
                    grille[py][px] = piece[y][x]
    return grille
@njit
def retirer_dernier_njit(grille, grille_originale, r_px, r_py, r_p):
        
    for y in range(3):
        for x in range(3):
            posx = r_px + x 
            posy = r_py + y 
            if 0<=posx<=5 and 0<=posy<=5 and r_p[y][x] >= 1:
                grille[posy][posx] = grille_originale[posy][posx]
    return grille

def rem_p(grille, idx):
    for i in range(len(grille.pieces)):
        if grille.pieces[i].idx == idx:
            return grille.pieces.pop(i)
        
def remplir_grille(grille):
    p=0
    piece_idx = grille.pieces_manquantes()[0]
    for piece in ttes_pieces_possibles[piece_idx]:  
        if verifier_njit(grille.grille, piece.piece, piece.x, piece.y) and verif_smileys_njit(grille1, piece.piece,piece.x,piece.y): 
            grille.ajouter(piece)
            grille.grille = mettre_dans_grille_njit(piece.piece,piece.x,piece.y, grille.grille)

            if grille.verif_complete():
                #update_game(grille.pieces)
                print(f"--GRILLE COMPLETE!!!!!!!!!-- IN {time.time()-start}")
                rem_piece=rem_p(grille, piece.idx)
                grille.grille = retirer_dernier_njit(grille.grille, grille1, rem_piece.x, rem_piece.y, rem_piece.piece)
                #pygame.image.save(win, f"img/{p+1}.jpg")
                return p+1
            
            else:
                
                p+=remplir_grille(grille) 
                #grille.retirer_dernier()
                rem_piece=rem_p(grille, piece.idx)
                grille.grille = retirer_dernier_njit(grille.grille, grille1, rem_piece.x, rem_piece.y, rem_piece.piece)

    return p


ttes_pieces_possibles = stuff(Grille(grille1))
for l in ttes_pieces_possibles:
    print(len(l))
nbTries=0
gr = Grille(np.copy(grille1))
#gr.ajouter(Pieces(8, r=1))
#gr.ajouter(Pieces(7, x=0, y=3, r=0, f=True))
#gr.ajouter(Pieces(6, x=4, y=0, r=0))
#gr.ajouter(Pieces(2, x=0, y=1, r=1, f=True))
#update_game(gr.pieces)
#ttes_pieces_possibles[0][1].afficher()
#ttes_pieces_possibles[0][0].flipper()
#ttes_pieces_possibles[0][0].afficher()
#input("begin")
#for p in ttes_pieces_possibles:
#    for piece in p:
#        update_game([piece])
#        print(piece)
#        input("cont.")

start = time.time()
print(f"il y a {remplir_grille(gr)} possibilites. Programme complété au bout de {time.time()-start} secondes.")

start = time.time()
print(f"il y a {remplir_grille(gr)} possibilites. Programme complété au bout de {time.time()-start} secondes.")
              


