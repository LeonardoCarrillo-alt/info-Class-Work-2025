import arcade
import pymunk

WIDTH = 800
HEIGHT = 800
TITLE = "hello physics"

class App(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLACK
        # fisicas
        self.space = pymunk.Space()
        self.space.gravity = (0, -90)

        # body
        body = pymunk.Body(mass=5, moment=pymunk.moment_for_box(1, (30, 30)))
        body.position = (WIDTH // 2, HEIGHT // 2)


        #floor body 
        floor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        floor_shape = pymunk.Segment(floor_body, (0, 20), (WIDTH, 20), 0)
        floor_shape.friction = 0.1
        floor_shape.elasticity = 0.7

        #shape
        self.shape = pymunk.Poly.create_box(body, (30, 30))
        self.shape.elasticity = 0.9
        self.shape.friction = 0.1

        # agregar al space
        self.space.add(body, self.shape)
        self.space.add(floor_body, floor_shape)

        # sprite
        self.sprites = arcade.SpriteList()
        self.body_sprite = arcade.SpriteSolidColor(30, 30, color=arcade.color.CYAN)
        self.sprites.append(self.body_sprite)

    def on_update(self, delta_time):
        self.space.step(1 / 60) # OJO
        # acoplar la posicion del body con el sprite
        self.body_sprite.center_x = self.shape.body.position.x
        self.body_sprite.center_y = self.shape.body.position.y
        self.body_sprite.radians = self.shape.body.angle
    
    def on_draw(self):
        self.clear()
        self.sprites.draw()

def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    game = App()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()