import arcade
import math
import numpy as np

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

    def apply_transform(self, TM):
        v_array = np.array([[x, y, 1] for x, y in self.vertices])
        v_array = np.transpose(v_array)
        # aplicar transformacion
        new_v_array = np.dot(TM, v_array)
        new_v_array = new_v_array[:2, :]
        new_v_array = np.transpose(new_v_array)
        self.vertices = new_v_array.tolist()
    
    def translate(self, dx, dy):
        TM = np.array([
            [1, 0, dx],
            [0, 1, dy],
            [0, 0, 1]
            ])
        self.apply_transform(TM)

    def scale(self, s):
        pass
    def rotate(self, angle, px=0, py=0):
        angle_radian = np.radians(angle)
        #T1 mover al origen 
        T1 = np.array([
            [1,0, -px],
            [0,1,+py],
            [0,0,1]
        ])
        TM = np.array([
            [np.cos(angle_radian), -np.sin(angle_radian), 0],
            [np.sin(angle_radian), np.cos(angle_radian), 1],
            [0, 0, 1]
        ])
        T3 = np.array([
            [1,0, px],
            [0,1,py],
            [0,0,1]
        ])
        TM = np.dot(T3, np.dot(TM, T1))
        self.apply_transform(TM)

class TransformView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLACK
        self.poly = Poly(points)
        self.poly2 = Poly(points, arcade.color.GREEN)
        self.poly2.translate(300, 300)

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