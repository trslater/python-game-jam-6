import arcade


class Player(arcade.Sprite):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            "assets/player.png",
            scale=1, image_width=16, image_height=16,
            *args, **kwargs)
