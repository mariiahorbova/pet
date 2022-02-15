import pygame


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize constant game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.bg = pygame.image.load("images/space.jpg")

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # Speed up scale
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initializing dynamic settings """
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction 1 is right; -1 -- left
        self.fleet_direction = 1

    def increase_speed(self):
        """ Speed up settings """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

