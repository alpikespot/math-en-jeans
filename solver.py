from pieces import Pieces
from grille import Grille
from enum import Enum
import time
import numpy as np

c_pieces = ["j", "j", "j", "o", "o", "r", "r", "n", "n"]

forbidden_cases_l = {
 "00": ["03", "30", "33"],
 "10": ["00", "03", "33"],
 "20": ["00", "30", "03"],
 "30": ["00", "30", "33"],

 "01": ["00", "03", "33"],
 "11": ["33", "03", "30"],
 "21": ["00", "30", "33"],
 "31": ["00", "03", "30"]
}

forbidden_cases_s = {
        #rotation, flip
        "00": [[0,0], [4,3]],
        "01": [[3,0], [-1,3]],
        "10": [[3,0], [0,4]],
        "11": [[0,0], [3,4]],
        "20": [[-1,0], [3,3]],
        "21": [[0,3], [4,0]],
        "30": [[0,3], [3,-1]],
        "31": [[0,-1],[3,3]]
        }

forbidden_cases_t = ["00", "03", "30", "33"]

"""
paramètres:
niveau log:
    -SILENCIEUX: sol. trouvée
    -BAVARD: sol. trouvée + actions 

niveau display:
    -AUCUN: pas d'affichage écran
    -SOLUTIONS: que les solutions trouvées
    -VALIDES: solutions trouvées + action valide
    -TOUT: solutions trouvées + action valide ou pas valide

MODE_RALENTI:
    -True: appuyer enter pour continuer programme
    -False: programme tourne lui-meme
    
"""

class Solver():
    def __init__(self, drawer):
        self.draw_component = drawer
        self.grille_vide = [
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]]
        
        self.pieces_valides = []
        self.solutions_ID = []
        
        self.affichage_enum = Enum('affichage_enum', [("RIEN",0), ("SOLUTION",1), ("VALIDE",2), ("TOUT",3)])
        self.opti_enum = Enum('opti_enum', [("AUCUNE", 0), ("EMPL_INTERDITS",1), ("QUE_SMILEYS", 2), ("VERIF_TROUS", 3)])

        self.event_enum = Enum('events', [("ENTER_FUNC",0),("EXIT_FUNC",1),("VERIF_PIECE",2), ("PIECE_BON", 3), ("PIECE_PAS_BON",4), ("GRILLE_VALIDE",5)])

        self.niveau_affichage = self.affichage_enum.VALIDE.value
        self.niveau_optimisation = self.opti_enum.AUCUNE.value
        self.MODE_RALENTI = True
        self.nb_smileys_grille = np.copy(self.grille_vide)

        self.MODE_INIT = True

        self.writeImg = input("mettre les images des solutions sur le disque? (risque de prendre bcp de place) y/N") == "y"

    def init_grille_dessiner(self,grille):
        if self.draw_component.dessiner_grille_smileys(grille)==1:
            self.MODE_INIT =False

    def trouver_emplacements_valides(self, grille):
        
        ttes_possibilites = [[],[],[],[],[],[],[],[],[]]
        for pieceIdx in range(9): 
            piece_coul = c_pieces[pieceIdx]
            rotnum = 4
            if pieceIdx == 7:
                flip = [False]
            else:
                flip = [False, True]
            
            for fl in flip:
                for rot in range(rotnum):
                    for xp in range(5 - int(rot%2==1)):
                        for yp in range(5 - int(rot%2==0)):
                        
                            xm = 0 ; ym = 0
                            if rot == 0:
                                xm = -int(fl)
                            if rot == 2:
                                xm = int(fl) - 1
                            if rot == 3:
                                ym = 1
                            xpos = xp+xm ; ypos = yp-ym
                            rotf_id = f"{rot}{int(fl)}"

                            pic = Pieces(pieceIdx, x=xpos, y=ypos, r=rot, f=fl)

                            if self.niveau_optimisation >self.opti_enum.AUCUNE.value:
                                if piece_coul == "o" or piece_coul == "r":
                                    if f"{xpos}{ypos}" in forbidden_cases_l[rotf_id]:
                                        continue
                                if piece_coul == "n":
                                    if f"{xpos}{ypos}" in forbidden_cases_t: 
                                        continue
                                if piece_coul == "j":
                                    if [xpos, ypos] in forbidden_cases_s[f"{rot}{int(fl)}"]:
                                        continue
                            if self.niveau_optimisation >= self.opti_enum.QUE_SMILEYS.value:
                                if not (grille.est_vide or (not grille.est_vide and grille.verif_smileys(pic))):
                                    continue

                            ttes_possibilites[pieceIdx].append(pic)

        return ttes_possibilites

    def resoudre_grille(self):
        
        grille_a_resoudre = self.grille_vide
        grille_obj = Grille(np.array(grille_a_resoudre, dtype=int))

        while self.MODE_INIT:
            self.init_grille_dessiner(grille_obj)

        self.nb_grilles_valides = 0

        self.niveau_affichage = int(input("Mettez le niveau d'affichage: \n-0:rien,\n-1:solutions,\n-2:valides,\n-3:tout\n.."))
        self.niveau_optimisation = int(input("Mettez le niveau d'optimisation: \n-0:aucune,\n-1:éliminer les emplacements interdits, \n-2:que les smileys, \n-3:vérification trous):\n.."))

        self.pieces_valides = self.trouver_emplacements_valides(grille_obj)
        
        
        if "y" in input("Afficher les pièces valides?"):
            for piece_idx in self.pieces_valides:
                for i in range(len(piece_idx)):
                    print(f"{piece_idx[i]} ({i}/{len(piece_idx)})")
                    self.draw_component.dessiner_appli(grille_obj, nouvelle_piece=piece_idx[i])
                    input("cont.")
        nb_possib_ss_col = 1
        for piece_idx in self.pieces_valides:
            nb_possib_ss_col = len(piece_idx) * nb_possib_ss_col
            print(f"{len(piece_idx)} * ",end="")
        print(f"1 = {nb_possib_ss_col} combinaisons possibles de pièces SANS PRENDRE EN COMPTE LES COLLISIONS.")
        input("Pret?")
        
        self.nb_essais = 0
        self.tps_debut = time.time()
        nb_solutions = self.trouver_solutions(grille_obj) #fonction récursive, trouve les solutions

        print(f"il y a {nb_solutions} possibilites. Programme complété au bout de {time.time()-self.tps_debut} secondes. {self.nb_essais} essais effectués. ")

    def trouver_solutions(self, grille):
        p=0
            
        piece_idx = grille.pieces_manquantes()[0] #la  pièce qu'on veut mettre
        self.broadcast(self.event_enum.ENTER_FUNC, grille)

        for i,piece in enumerate(self.pieces_valides[piece_idx]):  #pour chaque variation  de pièce (position, rotation, inversion différents) de la liste des pièces valides

            self.nb_essais += 1
                
            smileysVerif = grille.verif_smileys(piece)

            pieceEstValide = piece.verifier(grille) and smileysVerif
            if pieceEstValide and self.niveau_optimisation == self.opti_enum.VERIF_TROUS.value:
                pieceEstValide = grille.verif_entourage(piece)
            
            if pieceEstValide: #si on peut bien mettre la pièce dans la grille

                self.broadcast(self.event_enum.PIECE_BON, grille,piece=piece, id=i)
                grille.ajouter(piece)
                
                if len(grille.pieces_manquantes()) == 0:
                    
                    self.broadcast(self.event_enum.GRILLE_VALIDE, grille)

                    grille.retirer_dernier()

                    return 1
                
                else:    
                    p+=self.trouver_solutions(grille) 
                    grille.retirer_dernier()
            else:
                self.broadcast(self.event_enum.PIECE_PAS_BON, grille,piece=piece, id=i)
            
        self.broadcast(self.event_enum.EXIT_FUNC, grille)
        return p

    def charger_grille(self,id):
        grille = Grille(np.copy(self.grille_vide))
        grille.grille_from_id(id)

        self.draw_component.dessiner_appli(grille)
        input("voici la solution.")
        grille.pieces = []
        
        self.draw_component.dessiner_appli(grille)
        self.nb_smileys_grille = np.subtract(self.nb_smileys_grille,  grille.grille_originale)

    def faire_heatmap(self, path):
        self.nb_smileys_grille = np.copy(self.grille_vide)

        with open(path, "r") as f:
            grille_idx = 0
            
            while grille_idx<1525246:
                
                self.charger_grille(f.readline())

                #print(f"({grille_idx}/1525248)")
                print(grille_idx)
                self.draw_component.dessiner_heatmap(self.nb_smileys_grille)
                grille_idx += 1
            
            while True:
                self.draw_component.dessiner_heatmap(self.nb_smileys_grille)
            
    
    def broadcast(self, eventID, grille, piece=None, id=None):

        match eventID.value:
            case self.event_enum.ENTER_FUNC.value:
                if self.niveau_affichage >= self.affichage_enum.VALIDE.value:
                    print(f"--> Nouv. fonction. On va mettre la pièce  {grille.pieces_manquantes()[0]}")
                    self.draw_component.dessiner_appli(grille)

            case self.event_enum.EXIT_FUNC.value:
                if self.niveau_affichage >= self.affichage_enum.VALIDE.value:
                    print(f"<-- Quitter fonction (Impossible de mettre la pièce..)")
                    self.draw_component.dessiner_appli(grille)

            case self.event_enum.GRILLE_VALIDE.value:
                if self.niveau_affichage >= self.affichage_enum.SOLUTION.value:
                    self.nb_grilles_valides += 1
                            
                    self.solutions_ID.append(grille.get_grid_id())

                    if self.niveau_affichage >= self.affichage_enum.SOLUTION.value:
                        self.draw_component.dessiner_appli(grille)
                    if self.writeImg: 
                        self.draw_component.prendre_screen(grille)
                        
                    curt = time.time()-self.tps_debut
                    print(f"--GRILLE COMPLETE!-- IN {round(curt, 5)}s, ID:{self.nb_grilles_valides}, {round(self.nb_grilles_valides/curt, 5)} sol/s ", end="")
                    tdxt= grille.get_grid_id()
                    print(tdxt)

                    with open("solutions_grille.txt", "a") as f:
                        f.write(tdxt+"\n")
            
            case self.event_enum.PIECE_BON.value:
                if self.niveau_affichage >= self.affichage_enum.VALIDE.value:
                    print(f"Essayer de mettre la pièce {piece.idx} ({id}/{len(self.pieces_valides[piece.idx])}). ",end="")
                    print("on peut bien mettre la pièce.")
                    self.draw_component.dessiner_appli(grille, nouvelle_piece=piece)

            case self.event_enum.PIECE_PAS_BON.value:
                if self.niveau_affichage == self.affichage_enum.TOUT.value:
                    print(f"Essayer de mettre la pièce {piece.idx} ({id}/{len(self.pieces_valides[piece.idx])}). ",end="")
                    print("on peut PAS mettre la pièce.")

                    self.draw_component.dessiner_appli(grille,nouvelle_piece=piece)
        
        if self.MODE_RALENTI:
            if "f" in input("cont."):#input("Appuyez pour continuer.. (f pour désactiver le mode ralenti)"):
                self.niveau_affichage = self.affichage_enum.SOLUTION.value
                self.MODE_RALENTI = False


"""
9 pièces:
S2, S11, S12, LO1, LO2, LR1, LR2, T1, T2 
accompagné d'un vecteur entre 0 et 6 et rotation
6*6*4 = 144 possibilités par pièce
144 ** 9, c'est à dire ttes les possibilités possibles:
    2,67 * 10^19


Mode sans aucune optimisations:
    ~8500000 essais
Avec toutes les optimisations:
    ~41000 essais
"""

