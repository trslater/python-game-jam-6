import arcade

from pyjam.config import config
from pyjam.game import Game


def run():
    game = Game(
        config()["screen"]["width"],
        config()["screen"]["height"],
        config()["screen"]["title"])
    game.setup()
    arcade.run()
