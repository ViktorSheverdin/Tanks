import pygame
import pickle
from network import Network
from player import Player

width = 500
height = 500
window = pygame.display.set_mode((width,height))

def redraw_window(window, players_on_server):
    window.fill((255,255,255))
    for each_player_key, each_player_value in players_on_server.items():
        each_player_value.draw(window)
    pygame.display.update()

def get_players_on_server(network_module,obj_player):
    players_on_server = network_module.send({obj_player.playerID: obj_player})
    print("#######################################")
    print("players_on_server: ",players_on_server)
    print("#######################################")
    return players_on_server

def main():
    network_module = Network()
    clock = pygame.time.Clock()
    obj_player = network_module.getPlayerInfo()
    
    isRunning = True
    while isRunning:
        clock.tick(60)
        obj_player.move()

        players_on_server = get_players_on_server(network_module,obj_player)
        redraw_window(window,players_on_server)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()

main()