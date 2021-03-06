import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a Ship.
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    # Set the background color.
    #bg_color = (230, 230, 230)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            # You shouldn’t remove items from a list or group within a for loop, so
            # we have to loop over a copy of the group. We use the copy() method to set
            # up the for loop, which enables us to modify bullets inside the loop.
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        #print(len(bullets))
        
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
