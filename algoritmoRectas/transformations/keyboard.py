import arcade
import random
from game_object import Polygon2D

WIDTH = 800
HEIGHT = 800
TITLE = "Polygon2d"


def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )

class App(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLACK
        self.objects = []

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            for obj in self.objects:
                obj.scale(1.1, 1.1)
        elif symbol == arcade.key.DOWN:
            for obj in self.objects:
                obj.scale(0.9, 0.9)

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.objects.append(
                Polygon2D(
                    vertices=[
                        (x - 50, y - 50),
                        (x - 50, y + 50),
                        (x + 50, y + 50),
                        (x + 50, y - 50),
                    ],
                    color=get_random_color(),
                )
            )
            print(f"objetos: {len(self.objects)}")
        

    def on_draw(self):
        self.clear()
        for obj in self.objects:
            obj.draw()


def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    game = App()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()