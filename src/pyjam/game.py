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

        self.scene = None

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player")

        self.player_sprite = Player(self.pixel_size)
        self.player_sprite.center_x = self.width//2
        self.player_sprite.center_y = self.height//2

        self.scene.add_sprite("Player", self.player_sprite)

    def on_draw(self):
        """Render the screen."""

        self.clear()
        
        self.scene.draw(filter=NEAREST)
