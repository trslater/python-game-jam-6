import arcade


class Game(arcade.Window):
    def __init__(self, screen_width, screen_height, screen_title):

        # Call the parent class and set up the window
        super().__init__(screen_width, screen_height, screen_title)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        self.clear()
        # Code to draw the screen goes here