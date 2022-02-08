class GameStats:
    """Tracking stats of the game"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        # Start game in active state
        self.game_active = True

    def reset_stats(self):
        """Inizialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
