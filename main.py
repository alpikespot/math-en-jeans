"""
-commencer avec les pièces à 2 trous

"""
import pygame

from pieces import Pieces
from file import stuff
from grille import Grille
import numpy as np

import time
pygame.init()
win = pygame.display.set_mode((370, 370))
pygame.display.set_caption("Puzzle grille application")
clock = pygame.time.Clock()
writeImg = input("mettre les images des solutions sur le disque? (risque de prendre bcp de place) y/n") == "y"

with open("solutions_grille.txt", "w") as f:
    pass

grilles = [
    [[ 0, 0, 0, 0,-1, 0],
     [-1, 0,-1, 0, 0,-1],
     [ 0, 0, 0,-1, 0, 0],
     [ 0,-1, 0, 0, 0,-1],
     [ 0, 0,-1, 0, 0, 0],
     [-1, 0, 0, 0, 0,-1]],

    [[-1, 0, 0,-1, 0, 0],
    [ 0, 0, 0, 0,-1, 0],
    [ 0, 0, 0,-1, 0, 0],
    [-1,-1, 0, 0,-1, 0],
    [ 0,-1, 0,-1, 0, 0],
    [ 0, 0, 0, 0,-1, 0]],

    [[ 0, 0, 0, 0, 0, 0],
    [-1, 0,-1, 0,-1, 0],
    [ 0,-1, 0, 0, 0, 0],
    [-1, 0,-1, 0, 0,-1],
    [ 0, 0, 0,-1, 0, 0],
    [ 0,-1, 0, 0,-1, 0]],

    [[ 0,-1, 0,-1, 0, 0],
    [ 0, 0, 0, 0,-1, 0],
    [-1, 0,-1, 0, 0,-1],
    [ 0,-1, 0,-1, 0, 0],
    [ 0, 0, 0, 0, 0,-1],
    [ 0, 0,-1, 0, 0, 0]]

]
grille_vide = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

def update_game(pieces, piece_put):
    caseTaille = 50 
    ecartCase = 60

    win.fill(pygame.Color(0,0,0,255))
    gr = Grille(np.copy(grille1))
    for y in range(6):
        for x in range(6):
            valCase = gr.grille[y][x]
            
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
    
    if piece_put:
        piece_put.dessiner(win, gr)
    pygame.display.flip()
    #clock.tick(10)

def rem_p(grille, idx):
    for i in range(len(grille.pieces)):
        if grille.pieces[i].idx == idx:
            return grille.pieces.pop(i)
put = False
complete_grid_ids = []
validgridnum = 0

def remplir_grille(grille):
    p=0
    global nbTries, put, complete_grid_ids,validgridnum
        
    piece_idx = grille.pieces_manquantes()[0]
    
    for piece in ttes_pieces_possibles[piece_idx]:  

        nbTries += 1
        
        if piece.verifier(grille) and grille.verif_entourage(piece):
            grille.ajouter(piece)

            if len(grille.pieces_manquantes()) == 0:
                validgridnum += 1
                curt = time.time()-start
                print(f"--GRILLE COMPLETE!-- IN {round(curt, 5)}s, ID:{validgridnum}, {round(validgridnum/curt, 5)} sol/s  ", end="")
                print(grille.get_grid_id())
                complete_grid_ids.append(grille.get_grid_id())

                update_game(grille.pieces, None)
                if writeImg: 
                    pygame.image.save(win, f"img/g{GRILLE_NUM} {nbTries}.jpg")
                
                with open("solutions_grille.txt", "a") as file:
                    file.write(grille.get_grid_id() + "\n")
                grille.retirer_dernier()

                return 1
            
            else:    
                p+=remplir_grille(grille) 
                grille.retirer_dernier()

    return p

GRILLE_NUM = "0"
grille1 = np.array(grille_vide, dtype=int) #np.array(grilles[int(GRILLE_NUM)], dtype=int)

grille = np.copy(grille1)

ttes_pieces_possibles = stuff(Grille(np.copy(grille)))

nbTries = 0
grille = Grille(np.copy(grille))

start = time.time()
print(f"il y a {remplir_grille(grille)} possibilites. Programme complété au bout de {time.time()-start} secondes. {nbTries} essais effectués. ")



