class Player:
    def __init__(self, playerID, x, y, color, width, height):
        self.playerID = playerID
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

    def __str__(self):
        return " PlayerID: %s \n X: %s \n Y: %s \n Color: %s \n Width: %s \n Height: %s \n" % (self.playerID, self.x, self.y, self.color, self.width, self.height)

    def __repr__(self):
        return " PlayerID: %s \n X: %s \n Y: %s \n Color: %s \n Width: %s \n Height: %s \n" % (self.playerID, self.x, self.y, self.color, self.width, self.height)

p = Player(1,50,50,"blue",100,100)
print(p)