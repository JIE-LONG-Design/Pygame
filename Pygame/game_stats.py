class GameStats():

    def _init_(self, ai_settings):

        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):

        self.ships_left = self.ai_settings.ship_limit
