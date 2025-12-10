from pieces import Pieces
from grille import Grille
c_pieces = ["j", "j", "j", "o", "o", "r", "r", "n", "n"]
forbidden_cases_l = {
 "00": ["03", "30", "33"],
 "01": ["00", "03", "33"],
 "10": ["00", "03", "33"],
 "11": ["00", "03", "30"],
 "20": ["00", "30", "03"],
 "21": ["00", "30", "33"],
 "30": ["00", "30", "33"],
 "31": ["30", "03", "33"]
 }
forbidden_cases_s = {
        "00": [[0,0], [4,3]],
        "01": [[3,0], [-1,3]],
        "10": [[3,0], [0,4]],
        "11": [[0,0], [3,4]]
        }

forbidden_cases_t = ["00", "03", "30", "33"]

def stuff(grille):
    ttes_possibilites = [[],[],[],[],[],[],[],[],[]]
    for pieceIdx in range(9): 
        piece_coul = c_pieces[pieceIdx]
        rotnum = 4
        flip = [False, True]
        
        for rot in range(rotnum):
            for xp in range(5 - int(rot%2==1)):
                for yp in range(5 - int(rot%2==0)):

                    for fl in flip:
                        xm = 0 ; ym = 0
                        if rot == 0:
                            xm = -int(fl)
                        if rot == 2:
                            xm = int(fl) - 1
                        if rot == 3:
                            ym = 1
                        xpos = xp+xm ; ypos = yp-ym
                        rotf_id = f"{rot}{int(fl)}"
                        if piece_coul == "o" or piece_coul == "r":
                            if f"{xpos}{ypos}" in forbidden_cases_l[rotf_id]:
                                continue
                        if piece_coul == "n":
                            if f"{xpos}{ypos}" in forbidden_cases_t:
                                continue
                        if piece_coul == "j":
                            if [xpos, ypos] in forbidden_cases_s[f"{rot%2}{int(fl)}"]:
                                print("DOESNT WORK vvv", pieceIdx, xpos, ypos)
                                Pieces(pieceIdx, x=xpos, y=ypos, r=rot, f=fl).afficher()
                                #input(f"{xpos}, {ypos}, {rotf_id}")
                                
                                continue
                        pic = Pieces(pieceIdx, x=xpos, y=ypos, r=rot, f=fl)
                        #if piece_coul == "o":
                            #pic.afficher()
                        if grille.verif_smileys(pic):
                             ttes_possibilites[pieceIdx].append(pic)
    
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
 
