import pygame
import pickle
from network import Network
from player import Player

width = 500
height = 500
window = pygame.display.set_mode((width,height))

def redraw_window(window, current_player):
    window.fill((255,255,255))
    #pygame.draw.rect(window,obj_player.color, (obj_player.x,obj_player.y,obj_player.width,obj_player.height))
    current_player.draw(window)
    pygame.display.update()

def main():
    network_module = Network()
    clock = pygame.time.Clock()
    obj_player = network_module.getPlayerInfo()
    print("init obj_player: ", obj_player)
    
    isRunning = True
    while isRunning:
        #print("Getting player info")
        #print("New obj_play's ID is: \n", obj_player)
        clock.tick(60)

        obj_player.move()
        #print("ojb_player send: ",network_module.send(obj_player))
        players_on_server = network_module.send({obj_player.playerID: obj_player})
        print("#######################################")
        print("players_on_server: ",players_on_server)
        print("#######################################")
        
        window.fill((255,255,255))
        #for each_player_key, each_player_value in players_on_server.items():
        for each_player_key, each_player_value in players_on_server.items():
            print("each_player_value: ",each_player_value)
            print()
            #redraw_window(window, each_player)
            #pygame.draw.rect(window,each_player.color, (each_player.x,each_player.y,each_player.width,each_player.height))
            #redraw_window(window, each_player_value)
            #redraw_window(window, obj_player)
            pygame.draw.rect(window,each_player_value.color, (each_player_value.x,each_player_value.y,each_player_value.width,each_player_value.height))
        pygame.display.update()

            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()

main()