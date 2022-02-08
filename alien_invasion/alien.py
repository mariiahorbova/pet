import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A claas that represents one alien ship"""

    def __init__(self, ai_game):
        """Initialise an alien and set default position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load("images/alien_ship.png")
        self.image.set_colorkey((255, 255, 255))
        self.shrank_image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.shrank_image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
