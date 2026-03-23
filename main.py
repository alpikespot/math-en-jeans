


from pieces import Pieces
from grille import Grille
from solver import Solver
from renderer import Renderer


reponse = input("1: Démonstration du projet\n2: Charger une solution \n3: Trouver toutes les solutions possibles du JEU ENTIER (on nie les smileys)")[0]
drawer = Renderer()

match reponse:
    case "1":
        
        

        with open("solutions_grille.txt", "w") as f:
            pass
        solver = Solver(drawer)
        solver.resoudre_grille()
        
        input("..")
    case "2":
        solver = Solver(drawer)
        solver.charger_grille(input("Entrez l'identifiant de la grille: \n"))
        input("..")

    case "3":
        solver = Solver(drawer)
        solver.faire_heatmap("solutions_grille_big.txt")
        

    case "4":
        solver = Solver(drawer)
        solver.charger_grille()

        all_smileys_grid = []
        print("opening file..")
        with open("solutions_grille.txt", "r") as f:
            txt = f.read()
            i=0
            for gr_txt in txt.split("\n"):
                #grille.grille_from_id(gr_txt)
                all_smileys_grid.append(gr_txt)
                if i%100 == 0: print(i)
                i += 1
        print("file loaded.")
        #future_delete = []
        i = 0 ; j = 0
        print(f"num grids before: {len(all_smileys_grid)}")
        while i < len(all_smileys_grid):
            j = 0
            while j < len(all_smileys_grid):
                print(all_smileys_grid[i])
                if all_smileys_grid[i] == all_smileys_grid[j] and i != j:

                    print(f"same {i} {j}")
                    all_smileys_grid.pop(j)
                    j -= 1
                j += 1
            print(i)
            i += 1

        print(f"num grids after: {len(all_smileys_grid)}")
        
        with open("grille_smileys.txt", "w") as sm:
            for gr_smileys in all_smileys_grid:
                for y in range(len(gr_smileys)):
                    for x in range(len(gr_smileys)):
                        if gr_smileys[y][x] == -1:
                            sm.write(f"{x}{y}|")
                sm.write("\n")
            #grille_vide = gr_smileys
            #dessiner_appli([], None)

"""
--GRILLE COMPLETE!-- IN 2.83798s, ID:1, 0.35236 sol/s 01002|11135|21323|30331|41254|50204|61340|70310|80342|
il y a 1 possibilites. Programme complété au bout de 2.8784143924713135 secondes. 4673 essais effectués. 

14:
12591/6 326 480 160
0.0002% des essais

1:
41138/45 133 038 720
0.000091% des essais


"""