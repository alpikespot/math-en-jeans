from pieces import Pieces
from grille import Grille
def creer_file():  
  return []

def est_vide(f): 
  return f==[]

def enfiler(f,x): 
  return f.append(x)

def defiler(f): 
    return f.pop(0)

def stuff():
    file_pieces = creer_file()
    grille1 = [
    [0,0,0,0,-1,0],
    [-1,0,-1,0,0,-1],
    [0,0,0,-1,0,0],
    [0,-1,0,0,0,-1],
    [0,0,-1,0,0,-1],
    [-1,0,0,0,0,-1]]
    grille1 = Grille()
    nbPossibilites = 0
    ttes_possibilites = [[],[],[],[],[],[],[],[],[]]
    for pieceIdx in range(9): 
        file_pieces = []
        for x in range(6):
            for y in range(6):
                enfiler(file_pieces, Pieces(pieceIdx, x=x-1, y=y-1))

        for elt in range(len(file_pieces)):
            piece = defiler(file_pieces)
            posX = piece.x ; posY = piece.y 
            rotNum = 4
            for rot in range(rotNum):
                enfiler(file_pieces, Pieces(pieceIdx, x=posX, y=posY, r=rot))
                print(file_pieces[-1], end=" | ")
                if file_pieces[-1].verifier(grille1):
                    nbPossibilites += 1
                    print("Y")
                    ttes_possibilites[pieceIdx].append(file_pieces[-1])

                else:
                    print("N")
    return ttes_possibilites

def remplir_grilleee(grille):
    for pieceIdx in grille.pieces_manquantes(): #pour chaque pièce pas encore mise dans la grille
        for piece in ttes_pieces[pieceIdx]: # pour chaque POSITION et ROTATION possible d'une pièce choisie (avec pieceIdx)
            if piece.verifier(grille): #on verifie si on peut poser CETTE pièce (avec une POSITION et ROTATION précise) dans la grille 
                #si on peut, on l'ajoute
                print(f"--PIECE MISE, IDX == {pieceIdx} --")
                grille.ajouter(piece)
                
                if grille.verif_complete():
                    print(f"--GRILLE COMPLETE!!!!!!!!!--")
                    return grille.pieces
                else:
                    remplir_grille(grille)
            else:
                print("F", end="")
                continue #sinon, on essaye une autre POSITION et ROTATION de la pièce
            

#comp = 0
#ttes_pieces = stuff()
#remplir_grille(Grille())
        


"""
9 pièces:
S2, S11, S12, LO1, LO2, LR1, LR2, T1, T2 
accompagné d'un vecteur entre 0 et 6 et rotation
6*6*4 = 144 possibilités par pièce
144 ** 9, c'est à dire ttes les possibilités possibles:
    2,67 * 10^19

"""
 
