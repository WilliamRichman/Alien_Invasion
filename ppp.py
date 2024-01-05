import sys

import pygame 

def check_events(ship):
    #respond to inputs from user 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True    
                #move the ship right 
                #ship.rect.centerx +=1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False



def update_screen(ai_settings, screen, ship):
    ''' update the images on the screen and flip to a new screen '''
    #redraw the screen with each loop 
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()