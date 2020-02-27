import pygame
import pickle
from network import Network
from player import Player

width = 500
height = 500
window = pygame.display.set_mode((width,height))

def redraw_window(window, obj_player):
    window.fill((255,255,255))
    obj_player.draw(window)
    pygame.display.update()

def main():
    network_module = Network()
    #all_players = network_module.getAllPlayers()
    print("Getting player info")
    obj_player = network_module.getPlayerInfo()
    #print("Getting all player's info")
    #all_players = network_module.getAllPlayers()
    #all_players = network_module.send(obj_player)

    print("New obj_play's ID is: \n", obj_player)
    clock = pygame.time.Clock()


    isRunning = True
    while isRunning:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        obj_player.move()
        all_players = network_module.getAllPlayers()
        #network_module.send((network_module.getPlayerInfo()))
        # for each_player in all_players:
        #     print("Players in all_players: ", each_player)
        #     redraw_window(window, each_player)
        redraw_window(window, obj_player)

main()