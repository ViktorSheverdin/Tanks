import pygame
from network import Network
class Bullet():
    def __init__(self, bullet_id, playerID, x, y, direction):
        self.playerID = playerID
        self.vel = 10
        self.x = x
        self.y = y
        self.width = 12
        self.height = 12
        self.color = (100,100,100)
        self.direction = direction
        self.rect = (self.x,self.y,self.width,self.height)
        self.bullet_id = bullet_id
        self.exist = True

    def __str__(self):
        return "PlayerID: %s \n BulletID: %s \n Speed: %s \n X: %s Y: %s \n Width: %s \n Height: %s \n Color: %s \n Direction: %s \n Exist: %s \n" %(self.playerID,self.bullet_id,self.vel,self.x,self.y,self.width,self.height,self.color,self.direction,self.exist)

    def __repr__(self):
        return "PlayerID: %s \n BulletID: %s \n Speed: %s \n X: %s Y: %s \n Width: %s \n Height: %s \n Color: %s \n Direction: %s \n Exist: %s \n" %(self.playerID,self.bullet_id,self.vel,self.x,self.y,self.width,self.height,self.color,self.direction,self.exist)

    def get_bullet(self):
        return "PlayerID: %s \n BulletID: %s \n Speed: %s \n X: %s Y: %s \n Width: %s \n Height: %s \n Color: %s \n Direction: %s \n Exist: %s \n" %(self.playerID,self.bullet_id,self.vel,self.x,self.y,self.width,self.height,self.color,self.direction,self.exist)

    def increase_id_count(self):
        self.id_count += 1
    
    def check_for_collision(self,filed_width,filed_height):
        #bullet_moves = True
        #if self.x > filed_width-self.vel:
        if self.x > filed_width-self.width:
            self.exist = False
        elif self.x <= 1:
            self.exist = False
        elif self.y > filed_height-self.height:
            self.exist = False
        elif self.y <= 1:
            self.exist = False
        
        print("self.exist: %s"%(self.exist))
        return self.exist

    def move_bullet(self):
        print("Moving bullet")
        if self.direction == "EAST":
            self.x -= self.vel
        elif self.direction == "WEST":
            self.x += self.vel
        elif self.direction == "NORTH":
            self.y -= self.vel
        elif self.direction == "SOUTH":
            self.y += self.vel

        self.update()
        return (self.x, self.y)         

    def bullet_exists(self):
        if self.check_for_collision(500,500):
            self.move_bullet()
            return True
        else:
            print("Bullet is stopped")
            print("self.exist: %s"%(self.exist))
            return False      
    
    def draw(self, win):
        pygame.draw.rect(win,self.color, self.rect)

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)