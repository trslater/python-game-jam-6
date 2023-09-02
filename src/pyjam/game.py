from pathlib import Path
from random import randint

import arcade
from arcade.experimental import Shadertoy
from arcade.gl import NEAREST

from pyjam.player import Player


class Game(arcade.Window):
    def __init__(self, width, height, title, pixel_size):
        scaled_width = int(pixel_size*width)
        scaled_height = int(pixel_size*height)

        super().__init__(scaled_width, scaled_height, title,
                         antialiasing=False, fullscreen=False)
        
        arcade.set_background_color(arcade.color.FELDGRAU)

        self.pixel_size = pixel_size
        self.light_size = min(self.width, self.height)

        self.player_sprite = None
        self.scene = None
        self.camera = None

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)

        self.player_sprite = Player(self.pixel_size)
        self.player_sprite.center_x = self.width//2
        self.player_sprite.center_y = self.height//2
        self.scene.add_sprite("Player", self.player_sprite)

        for i in range(self.height//(16*self.pixel_size)):
            for j in range(self.width//(16*self.pixel_size)):
                if randint(0, 3) == 0:
                    wall = arcade.Sprite(
                        "assets/wall.png",
                        scale=self.pixel_size, image_width=16, image_height=16)
                    
                    wall.center_x = j*16*self.pixel_size
                    wall.center_y = i*16*self.pixel_size

                    self.scene.add_sprite("Walls", wall)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.scene.get_sprite_list("Walls"))
        
        self.camera = arcade.Camera(self.width, self.height)

        self.shadertoy = None
        self.channel0 = None
        self.channel1 = None
        self.load_shader()

    def load_shader(self):
        size = (2*self.width, 2*self.height)

        # # Create the shader toy
        self.shadertoy = Shadertoy.create_from_file(size, Path("assets/shadows.glsl"))

        # Create the channels 0 and 1 frame buffers.
        # Make the buffer the size of the window, with 4 channels (RGBA)
        self.channel0 = self.shadertoy.ctx.framebuffer(
            color_attachments=[self.shadertoy.ctx.texture(size, components=4)])
        self.channel1 = self.shadertoy.ctx.framebuffer(
            color_attachments=[self.shadertoy.ctx.texture(size, components=4)])

        # Assign the frame buffers to the channels
        self.shadertoy.channel_0 = self.channel0.color_attachments[0]
        self.shadertoy.channel_1 = self.channel1.color_attachments[0]

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

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )

        self.camera.move_to((screen_center_x, screen_center_y))

    def on_update(self, delta_time):
        """Movement and game logic"""

        self.physics_engine.update()
        self.center_camera_to_player()

    def on_draw(self):
        """Render the screen."""

        self.camera.use()

        self.channel0.use()
        self.channel0.clear()
        self.scene.draw(["Walls"], filter=NEAREST)

        self.use()
        self.clear()
        self.shadertoy.program['lightPosition'] = (self.width, self.height)
        self.shadertoy.program['lightSize'] = self.light_size
        self.shadertoy.render()
        self.scene.draw(["Player"], filter=NEAREST)
        self.scene.draw(["Walls"], filter=NEAREST)
