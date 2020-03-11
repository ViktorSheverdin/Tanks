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
        #player_bullets = each_player_value.get_list_of_bullets()        
        each_player_value.draw(window)
    for bullet_key,bullet_value in bullets_on_server.items():
        print("bullets_on_server: %s" %(bullets_on_server))
        print("Bullet type is: ", type(bullet_value))
        #updated_bullet = Bullet()
        #updated_bullet = bullet_value.get_bullet()
        #updated_bullet = bullet.__repr__()
        #print("updated_bullet: %s" %(updated_bullet))
        #updated_bullet.draw(window)
        #bullet_value = bullet_value.get_bullet()
        bullet_value.draw(window)
        #bullet["new_bullet"].draw(window)
    pygame.display.update()

def get_data_from_server(network_module, all_data_to_send):
    print("all_data_to_send: %s" %(all_data_to_send))
    data_from_server = network_module.send(all_data_to_send)
    #print("data_from_the_server: %s"%(data_from_server))
    return data_from_server

def get_players_on_server(network_module,obj_player):
    players_on_server = network_module.send({obj_player.playerID: obj_player})["players_on_server"]
    # print("#######################################")
    # print("players_on_server: ",players_on_server)
    # print("#######################################")
    return players_on_server

def get_bullets_on_server(network_module,obj_player,bullet):    
    bullet_id = "{0}b{1}".format(obj_player.playerID,bullet.id)
    print("bullet_id: %s" %(bullet_id))
    bullets = network_module.send({bullet_id: bullet})["bullets"]
    print("#######################################")
    print("bullets: ",bullets)
    print("#######################################")
    return bullets

def main():
    network_module = Network()
    clock = pygame.time.Clock()
    obj_player = network_module.getPlayerInfo()
    bullets_on_server = {}
    all_data_to_send = {}
    all_players_bullets = {}
    isRunning = True
    while isRunning:
        clock.tick(60)
        obj_player.move()
        #bullets = obj_player.get_list_of_bullets()
        #print("Bullets: %s" %(bullets))
        #obj_player.shoot()
        #all_data_to_send.update({obj_player.playerID: obj_player})
        all_data_to_send.update({"player": obj_player})
        all_data_to_send.update({"bullets":all_players_bullets})

        #all_data_to_send.update({"bullets": bullets})
        #print("all_data_to_send: %s" %(all_data_to_send))
        data_from_server = get_data_from_server(network_module,all_data_to_send)
        print("data_from_server: %s" %(data_from_server))
        #players_on_server = get_players_on_server(network_module,obj_player)
        players_on_server = data_from_server["players_on_server"]        
        #print("bullets_on_server type: %s" %(type(bullets_on_server)))
        #print("I AM HERE")
        bullets_on_server = data_from_server["bullets"]
        for each_bullet_key,each_bullet_value in bullets_on_server.items():
            #each_bullet_value.bullet_exists()
            #each_bullet_value.move_bullet()
            print("each_bullet exists: %s" %(each_bullet_value))

        redraw_window(window,players_on_server,bullets_on_server)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse is clicked")
                new_bullet = obj_player.shoot()
                print("Bullet was shot: ", new_bullet)
                print("Get bullet: ", new_bullet.get_bullet)
                
                # bullets_on_server = get_bullets_on_server(network_module,obj_player,new_bullet)
                # print("bullets_from_server: %s" %(bullets_on_server))
                # all_players_bullets.append({new_bullet})
                all_players_bullets.update({new_bullet.bullet_id:new_bullet})

main()