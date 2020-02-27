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
    clock = pygame.time.Clock()
    obj_player = network_module.getPlayerInfo()
    isRunning = True
    while isRunning:
        print("Getting player info")
        print("New obj_play's ID is: \n", obj_player)
        clock.tick(60)
        players_on_server = network_module.send(obj_player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        obj_player.move()
        #
        for each_player in players_on_server:
            redraw_window(window, each_player)

main()