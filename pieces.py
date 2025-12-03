c_pieces = ["o", "o", "r", "r", "n", "n", "j", "j", "j"]
import pygame
pieces = [
[[1,1,0], #les oranges
 [0,2,0],
 [0,1,0]],
 
 [[1,2,0],
  [0,1,0],
  [0,1,0]],

 [[2,1,0], #les rouges
  [0,1,0],
  [0,1,0]],

 [[1,1,0],
  [0,1,0],
  [0,2,0]],

 [[0,2,0],
  [1,1,1],
  [0,0,0]],
 
 [[0,1,0],
  [1,1,2],
  [0,0,0]],
 
 [[2,1,0],
  [0,2,1],
  [0,0,0]],
 
 [[2,1,0],
  [0,1,1],
  [0,0,0]],
[[1,1,0],
 [0,2,1],
 [0,0,0]]]
ecartCase = 60
caseTaille = 50
class Pieces():
    def __init__(self, idx, x=0, y=0, r=0):
        self.piece = pieces[idx]
        self.clr = (0,0,0,255)
        coul = c_pieces[idx]
        self.x = x
        self.y = y
        self.idx = idx
        self.rot = 0
        self.retourner(r)
        match coul:
            case "j": self.clr = (237, 212, 70, 255)
            case "n": self.clr = (95, 95, 95, 255)
            case "r": self.clr = (204, 54, 54, 255)
            case "o": self.clr = (228, 142, 42, 255)

    def retourner(self, rotIdx):
        for _ in range(rotIdx):
            self.piece = list(zip(*self.piece[::-1]))
            self.rot += 1
    def move(self, xPlus, yPlus):
        self.x += xPlus
        self.y += yPlus

    def __str__(self):
        return f"{self.idx}; ({self.y}, {self.x}) ; ({self.rot})"

    def verifier(self, grille):
        for y in range(3):
            for x in range(3):
                if self.piece[y][x] == 0:
                    continue

                if not 0<=(y+self.y)<6 or not (0<=(x+self.x)<6):
                    #print("piece out of bounds")
                    return False
                
                    #print(f"y:{y+self.y}, x:{x+self.x}")
                if grille.grille[y+self.y][x+self.x] > 0:
                    return False
        return True 
    
    def dessiner(self, scr, grille):
        estValide = self.verifier(grille)
        if estValide: 
            clr = self.clr
        else: 
            clr = (255,0,0,255)

        for y in range(3):
            for x in range(3):
                valCase = grille.grille[y][x]
                valPiece = self.piece[y][x]

                if valPiece != 0 and estValide:
                    pygame.draw.rect(scr, clr, (15 + (x+self.x) * ecartCase,15 + (y+self.y) * ecartCase, caseTaille-10, caseTaille-10))
                    
                

