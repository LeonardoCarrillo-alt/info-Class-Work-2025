import arcade
import math

WIDTH = 1280
HEIGHT = 720
TITLE = "hola arcade"

points = [
    (100, 100),
    (300, 100),
    (300, 300),
    (100, 300)
]

class Poly:
    def __init__(self, vertices, color=arcade.color.RED):
        self.vertices = vertices
        self.color = color
    
    def draw(self):
        arcade.draw_polygon_outline(self.vertices, self.color, 3)
    
    def translate(self, dx, dy):
        self.vertices = [(x + dx, y + dy) for x, y in self.vertices]
    
    def scale(self, s):
        self.vertices = [(x * s, y * s) for x, y in self.vertices]
    
    def rotate(self, angle, px=0, py=0):
        new_vertices = []
        angle_radians = math.radians(angle)
        for x, y in self.vertices:
            new_vertices.append(
                (
                    (x - px) * math.cos(angle_radians) - (y - py) * math.sin(angle_radians) + px,
                    (x - px) * math.sin(angle_radians) + (y - py) * math.cos(angle_radians) + py
                )
            )
        
        self.vertices = new_vertices

class TransformView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLACK
        self.poly = Poly(points)
        self.poly2 = Poly(points, arcade.color.GREEN)
        self.poly2.rotate(-75, 100, 100)

    def on_draw(self):
        self.clear()
        self.poly.draw()
        self.poly2.draw()


def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    game = TransformView()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()