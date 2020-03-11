import pygame
from bullet import Bullet
pygame.font.init()
class Player:
    def __init__(self, playerID, x, y, color, width, height):
        self.playerID = playerID
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.current_direction = "NORTH"
        self.bullets = []
        self.bullet_id = 0
        
        self.rect = (x,y,width,height)
        self.vel = 1

    def __str__(self):
        return " PlayerID: %s \n X: %s \n Y: %s \n Color: %s \n Width: %s \n Height: %s \n" % (self.playerID, self.x, self.y, self.color, self.width, self.height)

    def __repr__(self):
        return " PlayerID: %s \n X: %s \n Y: %s \n Color: %s \n Width: %s \n Height: %s \n" % (self.playerID, self.x, self.y, self.color, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win,self.color, self.rect)
        font = pygame.font.SysFont("comicsans", 20)
        text = font.render(str(self.playerID), 1, (0,0,0))
        win.blit(text, (100,150))
        #self.screen.blit(self.font.render(('PlayerID is: ',self.playerID), True, (255,0,0)), (200, 100))
        #pygame.draw.rect(win,(255,0,255), self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.current_direction = "EAST"
            self.x -= self.vel
            if self.x < 0:
                self.x = 0
        if keys[pygame.K_RIGHT]:
            self.current_direction = "WEST"
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.current_direction = "NORTH"
            self.y -= self.vel
            if self.y < 0:
                self.y = 0
        if keys[pygame.K_DOWN]:
            self.current_direction = "SOUTH"
            self.y += self.vel
        self.update()

    def shoot(self):        
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
            # bullet_x = self.x
            # bullet_y = self.y
        new_bullet = Bullet(self.playerID,self.x, self.y, self.current_direction)
        
        #self.bullets.append(new_bullet)
        #new_bullet.exist()
        
        return new_bullet

    def get_list_of_bullets(self):
        return self.bullets

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


# p = Player(1,50,50,"blue",100,100)
# print(p)