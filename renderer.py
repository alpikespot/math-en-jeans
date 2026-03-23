import pygame

class Renderer():
    def __init__(self):
        
        self.init_pygame()
        
    def init_pygame(self):
        
        pygame.init()
        self.win = pygame.display.set_mode((370, 370))
        pygame.display.set_caption("Puzzle grille application")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial",10)
    
    def prendre_screen(self, gr):
        pygame.image.save(self.win, f"img/g{GRILLE_NUM} {self.nb_essais}.jpg")
                    
        with open("solutions_grille.txt", "a") as file:
            file.write(gr.get_grid_id() + "\n")
    
    def dessiner_grille_smileys(self,gr):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        caseTaille = 50 
        ecartCase = 60
        self.win.fill(pygame.Color(0,0,0,255))

        #dessiner la grille
        for y in range(6):
            for x in range(6):
                caseRect = pygame.rect.Rect(10 + x*ecartCase, 10 + y*ecartCase, caseTaille, caseTaille)
                pygame.draw.rect(self.win, (200,200,200,255), caseRect)

                valCase = gr.grille_originale[y][x]

                if valCase==-1:
                    coul= (200, 200,50,255)
                else:
                    coul= (200,200,200,255)
                
                smileyRect = pygame.rect.Rect(15 + x * ecartCase + ecartCase/8 
                                                ,15 + y * ecartCase + ecartCase/8 , 
                                                (caseTaille-10)/1.5, 
                                                (caseTaille-10)/1.5)

                pygame.draw.rect(self.win, coul, smileyRect)


                if caseRect.collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()[0]:
                        gr.mettre_smiley(x,y)

                    elif pygame.mouse.get_pressed()[2]:
                        gr.retirer_smiley(x,y)
                    
        keys = pygame.key.get_pressed()

        if  keys[pygame.K_c]:
            return 1

        pygame.display.flip()
        
        self.clock.tick(60)
        return 0

    def dessiner_heatmap(self, gr_smileys):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        caseTaille = 50 
        ecartCase = 60
        self.win.fill(pygame.Color(0,0,0,255))
        maxsmileys=-1
        for row in gr_smileys:
            for s in row:
                if s>maxsmileys:
                    maxsmileys = s

        mpos = pygame.mouse.get_pos()
        #dessiner la grille
        for y in range(6):
            for x in range(6):
                #caseRect = pygame.rect.Rect(10 + x*ecartCase, 10 + y*ecartCase, caseTaille, caseTaille)
                #pygame.draw.rect(self.win, (200,200,200,255), caseRect)
                
                valCase = gr_smileys[y][x]

                coeff = valCase/maxsmileys

                coul = (255*coeff, 128*coeff, 64*coeff, 255)

                smileyRect = pygame.rect.Rect(15 + x * ecartCase + ecartCase/8 
                                                ,15 + y * ecartCase + ecartCase/8 , 
                                                (caseTaille-10)/1.5, 
                                                (caseTaille-10)/1.5)

                pygame.draw.rect(self.win, coul, smileyRect)

                if smileyRect.collidepoint(mpos):
                    surf = self.font.render(f"{round(coeff,3)} ({valCase}/{maxsmileys})", True, (255,255,255))
                    self.win.blit(surf, (mpos[0], mpos[1]-10))
        pygame.display.flip()

    def dessiner_appli(self, gr, nouvelle_piece=None):

        caseTaille = 50 
        ecartCase = 60

        self.win.fill(pygame.Color(0,0,0,255))

        #dessiner la grille
        for y in range(6):
            for x in range(6):
                pygame.draw.rect(self.win, (200,200,200,255), (10 + x*ecartCase, 10 + y*ecartCase, caseTaille, caseTaille))

                valCase = gr.grille[y][x]
                if valCase==-1:
                    coul= (200, 200,50,255)
                else:
                    coul= (200,200,200,255)
                
                pygame.draw.rect(self.win, coul, (15 + x * ecartCase + ecartCase/8 
                                                ,15 + y * ecartCase + ecartCase/8 , 
                                                (caseTaille-10)/1.5, 
                                                (caseTaille-10)/1.5))
        
        #dessiner les pièces sur la grille
        for piece in gr.pieces:
            piece.dessiner(self.win, gr)

        if nouvelle_piece:
            nouvelle_piece.dessiner(self.win, gr, nouvelle_piece.verifier(gr))

        pygame.display.flip()
        
        #clock.tick(10)