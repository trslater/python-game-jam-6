import arcade

from pyjam.config import config
from pyjam.game import Game


def run():
    game = Game(
        config()["screen"]["width"],
        config()["screen"]["height"],
        config()["screen"]["title"],
        config()["screen"]["pixel_size"])
    game.setup()
    arcade.run()
