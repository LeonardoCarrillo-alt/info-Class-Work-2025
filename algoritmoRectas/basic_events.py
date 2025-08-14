import arcade

WIDTH = 1280
HEIGHT = 720
TITLE = "eventos arcade"

class CircleCharacter:
    def __init__(self, x0, y0, r=50, color=arcade.color.RED):
        self.x = x0
        self.y = y0
        self.r = r
        self.color = color
        self.visible = False

    
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.color)

class EventsView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.YELLOW
        # estado de la app
        self.char = CircleCharacter(WIDTH // 2, HEIGHT // 2)
        self.speed = 4
        self.trail_points = []
        self.trail_points = []  # Puntos del rastro
        self.drawing_mode = True  # Modo de dibujo inicial
        self.current_line = []  # Línea que se está dibujando actualmente
        self.completed_lines = []  # Líneas completadas

    # 1. atencion de eventos
    def on_key_press(self, symbol, modifiers):
        ## teclado / joystick
        #if symbol == arcade.key.UP:
            # 2. actualizacion del estado
           # self.char.y += self.speed
       # elif symbol == arcade.key.DOWN:
          #  self.char.y -= self.speed
        if symbol == arcade.key.SPACE:
            # Cambiar entre modo dibujo y modo arrastre
            self.drawing_mode = not self.drawing_mode
            if not self.drawing_mode and self.current_line:
                self.completed_lines.append(self.current_line)
                self.current_line = []
                # Posicionar el círculo al final del último trazado
                if self.completed_lines:
                    last_line = self.completed_lines[-1]
                    if last_line:
                        self.char.x, self.char.y = last_line[-1]
                        self.char.visible = True

    def on_mouse_press(self, x, y, button, modifiers):
        print(f"boton presionado! {button} en posicion: {x}, {y}")
        # self.char.x = x
        # self.char.y = y
        if self.drawing_mode and button == arcade.MOUSE_BUTTON_LEFT:
            self.current_line.append((x, y))
            self.char.visible = False
    def on_mouse_drag(self, x, y, dx, dy, _buttons, _modifiers):
        print(f"arrastrando! {_buttons} en posicion: {x},{y}, con velocidad: {dx},{dy}")
        if self.drawing_mode and buttons == arcade.MOUSE_BUTTON_LEFT:
            self.current_line.append((x, y))
        elif not self.drawing_mode and self.char.visible:
            # Modo arrastre del círculo
            self.char.x += dx
            self.char.y += dy
            self.trail_points.append((self.char.x, self.char.y))
            # Limitar el tamaño del rastro
            if len(self.trail_points) > 100:
                self.trail_points.pop(0)
    # 3. renderizacion
    def on_draw(self):
        self.clear()
         # Dibujar todas las líneas completadas
        for line in self.completed_lines:
            if len(line) > 1:
                arcade.draw_points(line, arcade.color.BLUE, 4)
        
        # Dibujar la línea actual en proceso
        if self.current_line:
            arcade.draw_points(self.current_line, arcade.color.RED, 4)
        
        # Dibujar el rastro del círculo
        if self.trail_points:
            arcade.draw_points(self.trail_points, arcade.color.GREEN, 3)
        
        # Dibujar el círculo      # Dibujar el círculo encima
        self.char.draw()

        mode = "DIBUJO" if self.drawing_mode else "ARRASTRE"
        arcade.draw_text(f"Modo: {mode} (SPACE para cambiar)", 10, HEIGHT - 30, 
                         arcade.color.BLACK, 20)



def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    game = EventsView()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()