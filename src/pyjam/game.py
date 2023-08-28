import arcade

from pyjam.player import Player


class Game(arcade.Window):
    def __init__(self, screen_width, screen_height, screen_title):
        super().__init__(screen_width, screen_height, screen_title)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        self.player_list = arcade.SpriteList()

        self.player_sprite = Player()
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 400

        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """Render the screen."""

        self.clear()
        
        self.player_list.draw()
