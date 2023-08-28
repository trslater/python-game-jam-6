from random import randint

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
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)

        self.player_sprite = Player(self.pixel_size)
        self.player_sprite.center_x = self.width//2
        self.player_sprite.center_y = self.height//2

        for i in range(10):
            wall = arcade.Sprite(
                "assets/wall.png",
                scale=self.pixel_size, image_width=16, image_height=16)
            
            wall.center_x = randint(0, self.width - 16)
            wall.center_y = randint(0, self.height - 16)

            self.scene.add_sprite("Walls", wall)

        self.scene.add_sprite("Player", self.player_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.scene.get_sprite_list("Walls"))

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 5
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -5
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 5
    
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

    def on_draw(self):
        """Render the screen."""

        self.clear()
        
        self.scene.draw(filter=NEAREST)
