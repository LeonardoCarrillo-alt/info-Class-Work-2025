import arcade

WIDTH = 1000
HEIGHT = 500
TITLE = "Primitivas con arcade"

class PrimitivesView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.ALABAMA_CRIMSON
        self.a_pressed = False
        self.r_pressed = False

    def on_draw(self):
        self.clear()
        if self.a_pressed:
            self.background_color = arcade.color.MAGENTA
        elif self.a_pressed and not self.r_pressed:
            self.background_color = arcade.color.YELLOW
        elif not self.a_pressed and self.r_pressed:
            self.background_color = arcade.color.BLUE
        else: 
            self.background_color = arcade.color.RED
        #dibujar un punto (pixel)
        arcade.draw_point(500, 250, arcade.color.RED, 5)
        #dibujar secuencia de puntos
        arcade.draw_points(
            [(v, v) for v in range(100)],
            arcade.color.YELLOW, 2
        )
        #dibujar una linea
        #arcade.draw_line(500, 250, 700, 400, arcade.color.CYAN, 4)
        #arcade.draw_rect_filled(arcade.Rect(600, 700, 100, 500), arcade.color.GREEN)
        #arcade.draw_lrbt_rectangle_filled(600, 700, 100, 500, arcade.color.GREEN)
        #dibujar una cabeza
        arcade.draw_circle_filled(500, 350, 50, arcade.color.BABY_PINK, 0, -1)
        arcade.draw_lrbt_rectangle_filled(450, 550, 80, 300, arcade.color.GREEN )
        arcade.draw_lrbt_rectangle_filled(450, 480, 0, 100, arcade.color.BLUE )
        arcade.draw_lrbt_rectangle_filled(520, 550, 0, 100, arcade.color.BLUE )

    def on_key_press(self, symbol, modifiers) :
        if symbol == arcade.key.A:
            self.a_pressed = True
        elif symbol == arcade.key.R:
            self.r:pressed = True
    
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.A:
            self.background_color = arcade.color.RED
        elif symbol == arcade.key.R:
            self.background_color = arcade.color.RED
def main(): 
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    game = PrimitivesView()
    window.show_view(game)
    arcade.run()
if __name__ == "__main__":
    main()