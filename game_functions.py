import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()

            # Ship controls w,a,s,d
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    ship.moving_top = True
                elif event.key == pygame.K_a:
                     ship.moving_left = True
                elif event.key == pygame.K_s:
                     ship.moving_bottom = True
                elif event.key == pygame.K_d:
                     ship.moving_right = True
            elif event.type == pygame.KEYUP and event.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]:
                ship.moving_top = False
                ship.moving_left = False
                ship.moving_bottom = False
                ship.moving_right = False


def update_screen(setting, screen, ship):
    bg_image = pygame.image.load(setting.bg_image)
    bg_image = pygame.transform.scale(bg_image, (setting.screen_width, setting.screen_height))

    screen.blit(bg_image, (0, 0))
    ship.blitme()

    pygame.display.flip()
