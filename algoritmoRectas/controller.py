import arcade

WIDTH = 1280
HEIGHT = 720
TITLE = "hola arcade"

class ControllerView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.YELLOW
        self.controller = None
        self.x_joy, self.y_joy = 0, 0
        # controllers = arcade.get_controllers()
        controllers = arcade.get_game_controllers()
        print(f"encontrados {len(controllers)} controles!")
        # print(contr1)
        if controllers:
            self.controller = controllers[0]
            self.controller.open()
            self.controller.push_handlers(self)
            print("conectado a un control")
    
    # def on_joybutton_press(self, controller, button_name):
    #     # print(f"boton presionado: {button_name}")

    # def on_joybutton_release(self, controller, button_name):
    #     print(f"boton suelto: {button_name}")

    def on_joyaxis_motion(self, controller, axis, value):
        if axis == "x":
            self.x_joy = value
        elif axis == "y":
            self.y_joy = -value
        print(f"joystick: {axis} - {value}")

    def on_draw(self):
        self.clear()
        mid_point = WIDTH // 2, HEIGHT // 2
        end_point = mid_point[0] + int(self.x_joy * 100), mid_point[1] + int(self.y_joy * 100)

        arcade.draw_line(*mid_point, *end_point, arcade.color.BLUE, 4)



def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    game = ControllerView()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()