c_pieces = ["j", "j", "j", "o", "o", "r", "r", "n", "n"]
import numpy as np
import pygame
pieces = np.array([
 [[0,2,0], #les jaunes
  [2,1,0],
  [1,0,0]],
 
 [[0,2,0],
  [1,1,0],
  [1,0,0]],

[[0,1,0],
 [2,1,0],
 [1,0,0]],

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

 [[0,1,0], #les noires
  [2,1,0],
  [0,1,0]],
 
 [[0,2,0],
  [1,1,0],
  [0,1,0]]
 
 ])

forbidden_cases =  {"00": ["03", "30", "33"],
 "01": ["00", "03", "33"],
 "10": ["00", "03", "33"],
 "11": ["03", "00", "30"],
 "20": ["00", "30", "03"],
 "21": ["00", "30", "33"],
 "30": ["00", "30", "33"],
 "31": ["30", "03", "33"]}
ecartCase = 60
caseTaille = 50

class Pieces():
    
    def __init__(self, idx, x=0, y=0, r=0, f=False):
        self.piece = np.copy(pieces[idx])
        self.clr = (0,0,0,255)
        coul = np.array(c_pieces[idx])
        self.x = x
        self.flip = False
        self.y = y
        self.idx = idx
        self.rot = 0
        self.retourner(r)
        #print(self.piece)
        if f:
            self.flipper()
        match coul:
            case "j": self.clr = np.array([237, 212, 70, 255])
            case "n": self.clr = np.array([95, 95, 95, 255])
            case "r": self.clr = np.array([204, 54, 54, 255])
            case "o": self.clr = np.array([228, 142, 42, 255])

    def retourner(self, rotIdx):
        for _ in range(rotIdx):
            self.piece = np.array(list(zip(*self.piece[::-1])))
            self.rot += 1

    def move(self, xPlus, yPlus):
        self.x += xPlus
        self.y += yPlus

    def __str__(self):
        return f"{self.idx}; (y:{self.y}, x:{self.x}) ; r:({self.rot}) ; f:({self.flip})"
    
    def flipper(self):
        self.afficher()
        for i in range(len(self.piece)):
            self.piece[i] = self.piece[i][::-1]
        self.flip = not self.flip
        self.afficher()
        print("JAI FLIPPERR")
        #input("...")
    
    def verifier(self, grille):
        for y in range(3):
            for x in range(3):
                if self.piece[y][x] <= 0:
                    continue
                else:
                    if (not 0<=(y+self.y)<=5 or not (0<=(x+self.x)<=5)) or grille.grille[y+self.y][x+self.x] > 0:
                        #print("piece out of bounds")
                        return False
                
        return True 
    def afficher(self):
        for y in range(3):
            for x in range(3):
                if self.piece[y][x] >= 1:
                    val = "#"
                else:
                    val = " "
                print(val, end=" ")
            print("")
   
    def dessiner(self, scr, grille):
        estValide = self.verifier(grille) 
        if estValide: 
            clr = self.clr
        else: 
            clr = (255,0,0,255)

        for y in range(3):
            for x in range(3):
                
                valPiece = self.piece[y][x]
                posy=y+self.y;posx=x+self.x
                if valPiece != 0 and 0<=posx<=5 and 0<=posy<=5 and estValide:
                    valCase = grille.grille_originale[y+self.y][x+self.x]
                    pygame.draw.rect(scr, clr, (15 + (x+self.x) * ecartCase,15 + (y+self.y) * ecartCase, caseTaille-10, caseTaille-10))
                    if valPiece == 2:
                        if valCase==-1:
                            coul= (200, 200,50,255)
                        else:
                            coul= (200,200,200,255)
                        pygame.draw.rect(scr, coul, (15 + (x+self.x) * ecartCase + ecartCase/8 
                                                     ,15 + (y+self.y) * ecartCase + ecartCase/8 , 
                                                     (caseTaille-10)/1.5, 
                                                     (caseTaille-10)/1.5))

                    
                

