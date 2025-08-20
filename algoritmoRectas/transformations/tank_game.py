import arcade
import random
from game_object import Tank

WIDTH = 800
HEIGHT = 800
TITLE = "Polygon2d"

SPEED = 40
ANGULAR_SPEED = 1.5

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
        self.tank = Tank(400, 400, get_random_color())

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.tank.speed = SPEED
        if symbol == arcade.key.DOWN:
            self.tank.speed = -SPEED
        
        if symbol == arcade.key.LEFT:
            self.tank.angular_speed = ANGULAR_SPEED
        if symbol == arcade.key.RIGHT:
            self.tank.angular_speed = -ANGULAR_SPEED
        
        if symbol == arcade.key.R: 
            self.tank.shoot(110)
    
    def createminiTank(): 
        for _ in range (5): 
            self.tank = Tank(100, 100, get_random_color())
        

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.tank.speed = 0
        
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.tank.angular_speed = 0
    
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.tank.shoot(110)
        
    def on_update(self, delta_time: float):
        self.tank.update(delta_time)

    def on_draw(self):
        self.clear()
        self.tank.draw()


def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    game = App()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()