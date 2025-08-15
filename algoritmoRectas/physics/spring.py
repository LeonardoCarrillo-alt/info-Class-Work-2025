import arcade
import pymunk

# Constants
WIDTH = 800
HEIGHT = 600
TITLE = "Spring-Damper System Example"

# Physics parameters
MASS = 1.0
DAMPING = 0.5
STIFFNESS = 100.0
ANCHOR_POINT = (400, 500)
INITIAL_POSITION = (400, 300)

class App(arcade.View):
    def __init__(self):
        super().__init__()
        self.space = pymunk.Space()
        self.space.gravity = (0, -981)  # Gravity in pixels/second^2
        
        # Create the ball (dynamic body)
        body = pymunk.Body(MASS, pymunk.moment_for_circle(MASS, 0, 20))
        body.position = INITIAL_POSITION
        shape = pymunk.Circle(body, 20)
        shape.elasticity = 0.5
        self.space.add(body, shape)
        self.ball_sprite = arcade.SpriteCircle(20, color=arcade.color.BLUE)
        
        # Create the spring-damper (DampedSpring joint)
        anchor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        anchor_body.position = ANCHOR_POINT
        
        self.spring = pymunk.DampedSpring(
            anchor_body, body,  # Anchor and ball bodies
            (0, 0), (0, 0),  # Attachment points on the bodies
            rest_length=200, stiffness=STIFFNESS, damping=DAMPING
        )
        self.space.add(self.spring)
        
        # Anchor point
        self.anchor_sprite = arcade.SpriteCircle(10, color=arcade.color.RED)
        self.anchor_sprite.position = ANCHOR_POINT

        self.sprites = arcade.SpriteList()
        self.sprites.append(self.anchor_sprite)
        self.sprites.append(self.ball_sprite)

    def on_draw(self):
        self.clear()
        
        # Draw the anchor point
        self.sprites.draw()
        
        # Draw the spring as a line between the anchor and the ball
        arcade.draw_line(
            self.anchor_sprite.center_x, self.anchor_sprite.center_y,
            self.ball_sprite.center_x, self.ball_sprite.center_y,
            arcade.color.YELLOW, 2
        )

    def on_update(self, delta_time):
        self.space.step(1/60)
        self.ball_sprite.position = self.spring.b.position

def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    game = App()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()