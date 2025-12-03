"""
-commencer avec les pièces à 2 trous

"""
import pygame

from pieces import Pieces
from file import stuff
from grille import Grille
from copy import deepcopy
pygame.init()
win = pygame.display.set_mode((370, 370))
pygame.display.set_caption("Puzzle grille application")
clock = pygame.time.Clock()

grille1 = [
[0,0,0,0,-1,0],
[-1,0,-1,0,0,-1],
[0,0,0,-1,0,0],
[0,-1,0,0,0,-1],
[0,0,-1,0,0,-1],
[-1,0,0,0,0,-1]]

pieces_grille = []


def creer_file():  
  return []

def est_vide(f): 
  return f==[]

def enfiler(f,x): 
  return f.append(x)

def defiler(f): 
    return f.pop(0)

def creer_piece(pcs, idx):
    for piece in pcs:
        if piece.idx == idx:
            return False
    pcs.append(Pieces(idx))
    return pcs[len(pcs)-1]

grille = grille1
print("program begin")
running = True
piecePosX = 0; piecePosY = 0 ; rot = 0
pieceChoisie = 0
p_choisie = None
caseTaille = 50 
ecartCase = 60
file_pieces = creer_file()
pieceIdx = 0

for x in range(6):
    for y in range(6):
        enfiler(file_pieces, Pieces(pieceIdx, x=x, y=y))

def get_input():
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z: pieceChoisie += 1
            if event.key == pygame.K_s: pieceChoisie -= 1
            if event.key == pygame.K_LEFT: p_choisie.move(-1,0)
            if event.key == pygame.K_RIGHT: p_choisie.move(1,0)
            if event.key == pygame.K_DOWN: p_choisie.move(0,1)
            if event.key == pygame.K_UP: p_choisie.move(0, -1)
            if event.key == pygame.K_d: p_choisie.retourner(1) 
            if event.key == pygame.K_q: p_choisie.retourner(-1)
            if event.key == pygame.K_0: pieceChoisie = 0
            if event.key == pygame.K_1: pieceChoisie = 1 
            if event.key == pygame.K_5: pieceChoisie = 5
            if event.key == pygame.K_6: pieceChoisie = 6
            if event.key == pygame.K_7: pieceChoisie = 7
            if event.key == pygame.K_8: pieceChoisie = 8
            if event.key == pygame.K_o: 
                val_ret = creer_piece(pieces_grille, pieceChoisie)
                if val_ret != False: p_choisie = val_ret
        if event.type == pygame.QUIT:
            running = False

def update_game(pieces):
    #get_input()
    win.fill(pygame.Color(0,0,0,255))
    gr = Grille()
    for y in range(6):
        for x in range(6):
            #valCase = grille[y][x]
            
            pygame.draw.rect(win, (200,200,200,255), (10 + x*ecartCase, 10 + y*ecartCase, caseTaille, caseTaille))
            #if valCase == 1:
            #    pygame.draw.circle(win, (230,230,0,255), (10 + x*ecartCase + caseTaille/2, 10 + y*ecartCase + caseTaille/2), caseTaille/3)
    
    for piece in pieces:
        piece.dessiner(win, gr)
        if piece.verifier(gr): 
            gr.ajouter(piece)
    pygame.display.flip()
    clock.tick(60)

grille1 = Grille()
#print(f"PieceChoisie: {pieceChoisie}")
ttes_pieces_possibles = []
for elt in range(len(file_pieces)):
    piece = defiler(file_pieces)
    posX = piece.x ; posY = piece.y 

    for rot in range(4):
        enfiler(file_pieces, Pieces(6, x=posX-1, y=posY-1, r=rot))
        pieces_grille = [file_pieces[-1]]
        if pieces_grille[-1].verifier(grille1):
            ttes_pieces_possibles.append(pieces_grille[-1])

def remplir_grille(grille):
    print("--> Nouv. Fonction")
    grille.afficher()
    grille_original = deepcopy(grille)
    i = 0
    while i < len(grille.pieces_manquantes()):#pour chaque pièce pas encore mise dans la grille

        print(f"PIECES RESTANTES: {grille.pieces_manquantes()} | i = {i}")
        piece_idx = grille.pieces_manquantes()[i]
        print(f"ON VA METTRE LA  PIECE {piece_idx}")
        for piece in ttes_pieces_possibles[piece_idx]: # pour chaque POSITION et ROTATION possible d'une pièce choisie (avec pieceIdx)
            merged = grille.pieces + [piece]
            update_game(merged)
            if piece.verifier(grille) and not grille.verif_trous(piece): #on verifie si on peut poser CETTE pièce (avec une POSITION et ROTATION précise) dans la grille 
                #si on peut, on l'ajoute
                print(f"\n--PIECE MISE, IDX == {piece_idx} --")
                grille.ajouter(piece)
                
                
                if grille.verif_complete():
                    print(f"--GRILLE COMPLETE!!!!!!!!!--")
                    return grille.pieces
                else:
                    if not remplir_grille(grille): # Si on n'arrive pas à compléter a grille
                        grille = deepcopy(grille_original)
                        print(f"ON CONTINUE.. PIECES RESTANTES: {grille.pieces_manquantes()} | ON VA METTRE LA  PIECE {piece_idx} | i = {i}")
                        
                        #grille.afficher()
            else:
                print("F", end="")
                continue #sinon, on essaye une autre POSITION et ROTATION de la pièce
        print(f"\nEPIC FAIL, ON CHANGE DE PIECE")
        i += 1
    print(f"<-- Quit. Fonction")
    return False

def remplir_grille_no_print(grille):
    #print("--> Nouv. Fonction")
    #grille.afficher()
    grille_original = deepcopy(grille)
    i = 0
    while i < len(grille.pieces_manquantes()):#pour chaque pièce pas encore mise dans la grille

        #print(f"PIECES RESTANTES: {grille.pieces_manquantes()} | i = {i}")
        piece_idx = grille.pieces_manquantes()[i]
        #print(f"ON VA METTRE LA  PIECE {piece_idx}")
        for piece in ttes_pieces_possibles[piece_idx]: # pour chaque POSITION et ROTATION possible d'une pièce choisie (avec pieceIdx)
            merged = grille.pieces + [piece]
            #update_game(merged)
            if piece.verifier(grille): #on verifie si on peut poser CETTE pièce (avec une POSITION et ROTATION précise) dans la grille 
                print("VERIF TROUS...!!!!!")
                if grille.verif_trous(piece):
                    continue
                #si on peut, on l'ajoute
                #print(f"\n--PIECE MISE, IDX == {piece_idx} --")
                grille.ajouter(piece)
                update_game(merged)    
                
                if grille.verif_complete():
                    #print(f"--GRILLE COMPLETE!!!!!!!!!--")
                    return grille.pieces
                else:
                    if not remplir_grille_no_print(grille): # Si on n'arrive pas à compléter a grille
                        grille = deepcopy(grille_original)
                        print(f"ON CONTINUE.. PIECES RESTANTES: {grille.pieces_manquantes()} | ON VA METTRE LA  PIECE {piece_idx} | i = {i}")
                        
                        #grille.afficher()
            else:
                #print("F", end="")
                continue #sinon, on essaye une autre POSITION et ROTATION de la pièce
        #print(f"\nEPIC FAIL, ON CHANGE DE PIECE")
        i += 1
    #print(f"<-- Quit. Fonction")
    return False
ttes_pieces_possibles = stuff()
remplir_grille(Grille())

            
            


