import pygame 

class Ship():

    def __init__(self, ai_settings, screen):
        #Set ships starting position
        self.screen = screen 

        #Load ship imaage 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settiinigs = ai_settings
    #Start each new schip at center bottom position 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    #store a decimal value for ships center
        self.center = float(self.rect.centerx)
        #Movemnet Flag
        self.moving_right = False
        self.moving_left = False



    def update(self):
        #update the ships location 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settiinigs.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settiinigs.ship_speed_factor
        #update rect object from slef.center
        self.rect.centerx = self.center


    def blitme(self):
        #Draw the shop at current location 
        self.screen.blit(self.image, self.rect)





