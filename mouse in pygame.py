#  Import library
import pygame

# Initialize pygame
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("kaaryar project")

# Load images
player = pygame.image.load("images/dude1.png")
grass = pygame.image.load("images/grass.png")
badguy = pygame.image.load("images/badguy.png")

gate1 =  pygame.Rect((590, 330, 50, 150))
gate2 =  pygame.Rect((0, 0, 50, 150))
gameover_text = pygame.image.load("images/Game-Over.png")
ready_text = pygame.image.load("images/ready-text2.png")
nextlevel_text = pygame.image.load("images/next-level2.png")
winner_text = pygame.image.load("images/winner.png")
# obstacles of stage1
rect = player.get_rect(topleft=(0,50))
brect1 = badguy.get_rect(topleft=(100, 0))
brect2 = badguy.get_rect(topleft=(10, 200))
brect3 = badguy.get_rect(topleft=(50, 300))
brect4 = badguy.get_rect(topleft=(200, 250))
brect5 = badguy.get_rect(topleft=(300, 300))
brect6 = badguy.get_rect(topleft=(500, 400))
# obstacles of stage2
brect7 = badguy.get_rect(topleft=(100, 100))
brect8 = badguy.get_rect(topleft=(400, 200))
brect9 = badguy.get_rect(topleft=(400, 30))
brect10 = badguy.get_rect(topleft=(200, 250))
brect11= badguy.get_rect(topleft=(300, 300))
brect12= badguy.get_rect(topleft=(60, 400))

#movement speed
vel = 3

#........................................................................................................................
#......................GAME STATE CLASS..................................................................................
class GameState:
    def __init__(self):
        self.state = "intro"
    
    #INTRO    
    def intro(self):

                
        #adding appearence
        for x in range(int(width/grass.get_width()+1)):
            for y in range(int(height/grass.get_height()+1)):
                screen.blit(grass,(x*100,y*100))
        screen.blit(ready_text,(150, 60))
        
        
        pygame.display.flip()
        #  event hanler
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT:
                
                pygame.quit() 
                exit()
        #begin the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "stage1" 
                        
    #NEXT LEVEL          
    def next_level(self):

        #adding appearence
        for x in range(int(width/grass.get_width()+1)):
            for y in range(int(height/grass.get_height()+1)):
                screen.blit(grass,(x*100,y*100))
        screen.blit(nextlevel_text,(130, 60))
        
        
        pygame.display.flip()
        #  event hanler
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT:
                
                pygame.quit() 
                exit()
            if rect.colliderect(gate1):
                print(".........congratulation........")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = "stage2"
    
    #WINNER            
    def winner(self):

        #adding appearence
        
        for x in range(int(width/grass.get_width()+1)):
            for y in range(int(height/grass.get_height()+1)):
                screen.blit(grass,(x*100,y*100))
        screen.blit(winner_text,(130, 60))
        
        
        pygame.display.flip()
        #  event hanler
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit() 
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
        if rect.colliderect(gate1):
            print(".........congratulation........")
                         
    #STAGE 1               
    def stage1(self):
        
        #adding appearence
        for x in range(int(width/grass.get_width()+1)):
            for y in range(int(height/grass.get_height()+1)):
                screen.blit(grass,(x*100,y*100))
               
        pygame.draw.rect(screen, (255, 0, 0), gate1)
        pygame.draw.rect(screen, (255, 0, 0), gate2)   
        screen.blit(badguy, brect1)
        screen.blit(badguy, brect2)
        screen.blit(badguy, brect3)
        screen.blit(badguy, brect4)
        screen.blit(badguy, brect5)
        screen.blit(badguy, brect6)
        
        screen.blit(player, rect)
        
        pygame.display.flip()
        #  loop through the events
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT:
                
                pygame.quit() 
                exit(0)     
                          
            #player movement
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_LEFT]:
            rect.x -= vel
        if userInput[pygame.K_RIGHT]:
            rect.x += vel
        if userInput[pygame.K_UP]:
            rect.y -= vel
        if userInput[pygame.K_DOWN]:
            rect.y += vel
            
        # COLLISION CHEKING
        if rect.colliderect(brect1):
            pygame.draw.rect(screen, (255, 0, 0), rect, 4)# draw red box around player
            self.state = "gameover"# show game over page 
        if rect.colliderect(brect2):
            pygame.draw.rect(screen, (255, 0, 0), rect, 4)# draw red box around player
            self.state = "gameover"# show game over page 
        if rect.colliderect(brect3):
            pygame.draw.rect(screen, (255, 0, 0), rect, 4)# draw red box around player
            self.state = "gameover"# show game over page 
        if rect.colliderect(brect4):
            pygame.draw.rect(screen, (255, 0, 0), rect, 4)# draw red box around player
            self.state = "gameover"# show game over page 
        if rect.colliderect(brect5):
            pygame.draw.rect(screen, (255, 0, 0), rect, 4)# draw red box around player
            self.state = "gameover"# show game over page 
        if rect.colliderect(brect6):
            pygame.draw.rect(screen, (255, 0, 0), rect, 4)# draw red box around player
            self.state = "gameover"# show game over page 
        #  NEXT LEVEL
        if rect.colliderect(gate1):
                self.state = "next_level"
                 
    #STAGE 2
    def stage2(self):
        
        #adding appearence
        for x in range(int(width/grass.get_width()+1)):
            for y in range(int(height/grass.get_height()+1)):
                screen.blit(grass,(x*100,y*100))
        screen.blit(badguy, brect7)
        screen.blit(badguy, brect8)
        screen.blit(badguy, brect9)
        screen.blit(badguy, brect10)
        screen.blit(badguy, brect11)
        screen.blit(badguy, brect12)
        pygame.draw.rect(screen, (255, 0, 0), gate1)
        pygame.draw.rect(screen, (255, 0, 0), gate2)
        player = pygame.image.load("images/dude2.png")
        screen.blit(player, rect)
        
        pygame.display.flip()
        #  loop through the events
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT:
                
                pygame.quit() 
                exit(0)     
        
            #player movement
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_LEFT]:
            rect.x -= vel
        if userInput[pygame.K_RIGHT]:
            rect.x += vel
        if userInput[pygame.K_UP]:
            rect.y -= vel
        if userInput[pygame.K_DOWN]:
            rect.y += vel
            
        if rect.colliderect(gate2):
                self.state = "winner" 
        # COLLISION CHEKING
        if rect.colliderect(brect7):
            pygame.draw.rect(screen, (255, 0, 0), rect, 4)# draw red box around player
            self.state = "gameover"# show game over page 
        if rect.colliderect(brect8):
            pygame.draw.rect(screen, (255, 0, 0), rect, 4)# draw red box around player
            self.state = "gameover"# show game over page 
        if rect.colliderect(brect9):
            pygame.draw.rect(screen, (255, 0, 0), rect, 4)# draw red box around player
            self.state = "gameover"# show game over page 
        if rect.colliderect(brect10):
            pygame.draw.rect(screen, (255, 0, 0), rect, 4)# draw red box around player
            self.state = "gameover"# show game over page 
        if rect.colliderect(brect11):
            pygame.draw.rect(screen, (255, 0, 0), rect, 4)# draw red box around player
            self.state = "gameover"# show game over page 
        if rect.colliderect(brect12):
            pygame.draw.rect(screen, (255, 0, 0), rect, 4)# draw red box around player
            self.state = "gameover"# show game over page    
            
    #GAME OVER           
    def gameover(self):

        #adding appearence
        for x in range(int(width/grass.get_width()+1)):
            for y in range(int(height/grass.get_height()+1)):
                screen.blit(grass,(x*100,y*100))
        screen.blit(gameover_text,(150, 60))
        
        
        pygame.display.flip()
        #  event hanler
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT:
                
                pygame.quit() 
                exit()
        #begin the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()  
         
    #STAGE MANAGER 
    def stage_manager(self):
        if self.state == "intro":
            self.intro()
    
        if self.state == "stage1":
            self.stage1()
            
        if self.state == "stage2":
            self.stage2()
        
        if self.state == "gameover":
            self.gameover()
            
        if self.state == "next_level":
            self.next_level()
            
        if self.state == "winner":
            self.winner()
  
#.....................................................................................................................            
#GAME STATE CHANGER
game_state = GameState()


# game loop
while 1:
    game_state.stage_manager()
  
   
    

