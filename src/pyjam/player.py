import arcade


class Player(arcade.Sprite):
    def __init__(self, pixel_size, *args, **kwargs) -> None:
        super().__init__(
            "assets/player.png",
            scale=pixel_size, image_width=16, image_height=16,
            *args, **kwargs)
