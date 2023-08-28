import arcade
from arcade.gl import NEAREST

from pyjam.player import Player


class Game(arcade.Window):
    def __init__(self, width, height, title, pixel_size):
        width *= pixel_size
        height *= pixel_size

        super().__init__(width, height, title,
                         antialiasing=False, fullscreen=True)

        self.pixel_size = pixel_size

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        self.player_list = arcade.SpriteList()

        self.player_sprite = Player(self.pixel_size)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 400

        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """Render the screen."""

        self.clear()
        
        self.player_list.draw(filter=NEAREST)
