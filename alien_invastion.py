import pygame

from settings import Settings
from ship import Ship
import game_functions as gf



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("William's Alien Invation")


    #make ship
    ship = Ship(ai_settings, screen)


    #While loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
    

#        screen.fill(ai_settings.bg_color)
#        ship.blitme()
#        pygame.display.flip()



#end of run_game
run_game()