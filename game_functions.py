import sys

import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT: #Check if key is right key
        ship.moving_right = True
    elif event.key == pygame.K_LEFT: 
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:   #Each keypress is registered with KD
            check_keydown_events(event, ai_settings, screen, ship, bullets)
            '''
            if event.key == pygame.K_RIGHT: #Check if key is right key
                ship.rect.centerx += 1
                ship.moving_right = True
            elif event.key == pygame.K_LEFT: 
                ship.moving_left = True
            '''
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            '''
            if event.key == pygame.K_RIGHT:
                #ship.rect.centerx += 1
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            '''

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        # You shouldn’t remove items from a list or group within a for loop, so
        # we have to loop over a copy of the group. We use the copy() method to set
        # up the for loop, which enables us to modify bullets inside the loop.
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
