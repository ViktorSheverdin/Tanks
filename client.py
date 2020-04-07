import pygame
import pickle
from network import Network
from player import Player
from bullet import Bullet

field_width = 500
field_height = 500
window = pygame.display.set_mode((field_width,field_height))

def redraw_window(window, players_on_server,bullets_on_server):
    window.fill((255,255,255))
    for each_player_key, each_player_value in players_on_server.items():
        each_player_value.draw(window)
    for bullet_key,bullet_value in bullets_on_server.items():
        bullet_value.draw(window)
    pygame.display.update()

def get_data_from_server(network_module, all_data_to_send):
    print("all_data_to_send: %s" %(all_data_to_send))
    data_from_server = network_module.send(all_data_to_send)
    #print("data_from_the_server: %s"%(data_from_server))
    return data_from_server

# def get_players_on_server(network_module,obj_player):
#     players_on_server = network_module.send({obj_player.playerID: obj_player})["players_on_server"]
#     # print("#######################################")
#     # print("players_on_server: ",players_on_server)
#     # print("#######################################")
#     return players_on_server

# def get_bullets_on_server(network_module,obj_player,bullet):    
#     bullet_id = "{0}b{1}".format(obj_player.playerID,bullet.id)
#     print("bullet_id: %s" %(bullet_id))
#     bullets = network_module.send({bullet_id: bullet})["bullets"]
#     print("#######################################")
#     print("bullets: ",bullets)
#     print("#######################################")
#     return bullets

def main():
    network_module = Network()
    clock = pygame.time.Clock()
    obj_player = network_module.getPlayerInfo()
    all_data_to_send = {}
    all_players_bullets = {}
    isRunning = True
    while isRunning:
        clock.tick(60)
        obj_player.move()
        
        all_data_to_send.update({"player": obj_player})
        all_data_to_send.update({"bullets":all_players_bullets})
        
        data_from_server = get_data_from_server(network_module,all_data_to_send)
        players_on_server = data_from_server["players_on_server"]
        bullets_on_server = data_from_server["bullets"]
        all_players_bullets.clear()

        redraw_window(window,players_on_server,bullets_on_server)

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
                
            if keys[pygame.K_SPACE]:
                new_bullet = obj_player.shoot()
                all_players_bullets.update({new_bullet.bullet_id:new_bullet})

main()