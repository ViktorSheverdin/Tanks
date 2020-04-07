import pygame
from network import Network
from bullet import Bullet

class GameManager():
    def __init__(self):
        self.name = "GameMenager"

def move_bullet():
    pass

def get_data_from_server(network_module, all_data_to_send):
    print("all_data_to_send: %s" %(all_data_to_send))
    data_from_server = network_module.send(all_data_to_send)
    print("data_from_the_server: %s"%(data_from_server))
    return data_from_server

def main():    
    all_data_to_send = {}
    all_players_bullets = {}
    bullets_to_delete = {}
    network_module = Network()
    gM = network_module.connect()
    print("gM: %s"%(gM))
    gameManager = GameManager()
    obj_player = network_module.getPlayerInfo()
    clock = pygame.time.Clock()
    isRunning = True

    while isRunning:
        clock.tick(60)

        all_data_to_send.update({"player": obj_player})
        all_data_to_send.update({"bullets":all_players_bullets})
        all_data_to_send.update({"bullets_to_delete":bullets_to_delete})
        data_from_server = get_data_from_server(network_module,all_data_to_send)
        bullets_on_server = data_from_server["bullets"]

        for each_bullet_key,each_bullet_value in bullets_on_server.items():
            each_bullet_value.bullet_exists()
            all_players_bullets.update({each_bullet_key:each_bullet_value})

main()