import arcade

WIDTH = 1280
HEIGHT = 720
TITLE = "hola arcade"
MOVEMENT_SPEED = 8

class Player(arcade.Sprite):
    def update(self, delta_time: float = 1/60):
        self.center_x += self.change_x
        self.center_y += self.change_y


class KeyboardMovementView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLACK
        self.sprite_list = arcade.SpriteList()
        self.player = Player(
            "algoritmoRectas/img/mario.png", 
            center_x=WIDTH // 2,
            center_y=HEIGHT // 2
            )
        self.sprite_list.append(self.player)

    def on_update(self, delta_time):
        self.sprite_list.update(delta_time)

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()
    
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif symbol == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif symbol == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED
        elif symbol == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED

    def on_key_release(self, symbol, modifiers):
        if symbol in [arcade.key.UP, arcade.key.DOWN]:
            self.player.change_y = 0
        elif symbol in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.change_x = 0
                
            

def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    game = KeyboardMovementView()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()