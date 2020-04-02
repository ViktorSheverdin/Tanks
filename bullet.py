import pygame
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
        # self.id_count = 0
        # self.bullet_id = "{0}b{1}".format(self.playerID,self.id_count)
        # self.increase_id_count()
        self.bullet_id = bullet_id

    def __str__(self):
        return "PlayerID: %s \n BulletID: %s \n Speed: %s \n X: %s Y: %s \n Width: %s \n Height: %s \n Color: %s \n Direction: %s" %(self.playerID,self.bullet_id,self.vel,self.x,self.y,self.width,self.height,self.color,self.direction)

    def __repr__(self):
        return "PlayerID: %s \n BulletID: %s \n Speed: %s \n X: %s Y: %s \n Width: %s \n Height: %s \n Color: %s \n Direction: %s" %(self.playerID,self.bullet_id,self.vel,self.x,self.y,self.width,self.height,self.color,self.direction)

    def get_bullet(self):
        #return {self.playerID,self.bullet_id,self.vel,self.x,self.y,self.width,self.height,self.color}
        return "PlayerID: %s \n BulletID: %s \n Speed: %s \n X: %s Y: %s \n Width: %s \n Height: %s \n Color: %s \n Direction: %s" %(self.playerID,self.bullet_id,self.vel,self.x,self.y,self.width,self.height,self.color,self.direction)


    def increase_id_count(self):
        self.id_count += 1
    
    def check_for_collision(self,filed_width,filed_height):
        bullet_moves = True
        #if self.x > filed_width-self.vel:
        if self.x > filed_width-self.width:
            bullet_moves = False
        elif self.x <= 1:
            bullet_moves = False
        elif self.y > filed_height-self.height:
            bullet_moves = False
        elif self.y <= 1:
            bullet_moves = False
        # if not bullet_moves:
        #     self.color = (0,200,200)
        print("Checking for collision bullet_moves", bullet_moves)
        return bullet_moves

    def move_bullet(self):
        print("Moving bullet")
        if self.direction == "EAST":
            print("Before, self.x is: %s" %(self.x))
            self.x -= self.vel
            print("After, self.x is: %s" %(self.x))
        elif self.direction == "WEST":
            self.x += self.vel
        elif self.direction == "NORTH":
            self.y -= self.vel
        elif self.direction == "SOUTH":
            self.y += self.vel
        
        print("new x: %s new y: %s"%(self.x,self.y))

        self.update()
        return (self.x, self.y)

    # def exist(self):
    #     bullet_moves = True
    #     while bullet_moves:
    #         print("Start the loop")
    #         bullet_moves = self.check_for_collision(500,500)
    #         self.move_bullet()
    #         print("Bullet moves. X: %s Y: %s " %(self.x, self.y))
    #         #self.draw(pygame.display.set_mode((500,500)))

    def bullet_exists(self):
        if self.check_for_collision(500,500):
            self.move_bullet()
            return True
        else:
            return False

    def draw(self, win):
        pygame.draw.rect(win,self.color, self.rect)
        #pygame.display.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)