import arcade

WIDTH = 1280
HEIGHT = 720
TITLE = "Hello Arcade"

class HelloView(arcade.View):

    #definir la parte de la pantalla
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.AMAZON
    def reset(self):
        pass
    def on_draw(self):
        self.clear()
        #para pintar pixeles
        arcade.draw_point(WIDTH // 2, HEIGHT // 2, arcade.color.BLUE, 1)
        #self.draw_vertical_line(640, 0, 640, 360, arcade.color.RED)
        self.draw_bresenham_line(100, 100, 1100, 650)
        self.draw_bresenham_line_2(100, 100, 150, 300) 
        self.draw_bresenham_line_2(300, 300, 150, 100)
        self.draw_bresenham_line_2(100, 100, 150, 300)
    
    #def draw_vertical_line(self, x0, y0, x1, y1, color):
     #   assert x0 == x1 
      #  for y in range (y0, y1 + 1): 
       #     arcade.draw_point(x0, y, arcade.color.RED, size= 1)
    def draw_bresenham_line(self, x0, y0, x1, y1):
        dx,dy = x1 - x0, y1 - y0 
        xk = x0
        yk =y0
        points = [(x0, y0)]
        Pk = 2 * dy - dx
        while xk < x1:
            xk += 1
            if Pk > 0: 
                yk += 1
                Pk = Pk + 2 * dy -2 * dx
            else:
                Pk = Pk + 2 * dy
                arcade.draw_point(xk, yk, arcade.color.BLUE, size = 4)
            points.append((xk, yk))
        return points

    def draw_bresenham_line_2 (self, x0, y0, x1, y1):
        dx, dy = x1 - x0, y1 - y0
        det = abs(dy)>abs(dx)
        #para det (2, 3, 6, 7), intercambiamos x y y
        if det: 
            x0, y0 = y0, x0
            x1, y1 = y1, x1
            dx, dy = dy, dx
        #Si la línea va hacia atrás (octantes 4,5,6,7), invertir dirección
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
            dx = -dx
            dy = -dy
        
        # Bresenham para primer octante (0 ≤ m ≤ 1, x1 > x0)
        points = []
        Pk = 2 * dy - dx
        y = y0
        y_step = 1 if dy > 0 else -1  # Manejar octantes 5,8 (pendiente negativa)
        
        for x in range(x0, x1 + 1):
            # Mapear de vuelta si se hizo steep
            if det:
                points.append((y, x))  # Intercambiar x y y
                arcade.draw_point(y, x, arcade.color.BLUE, size = 4)
            else:
                points.append((x, y))
                arcade.draw_point(x, y, arcade.color.RED, size = 4)
            
            # Actualizar Pk y y
            if Pk > 0:
                y += y_step
                Pk += 2 * (dy - dx)
            else:
                Pk += 2 * dy
        
        return points

    
def main(): 
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    game = HelloView()
    window.show_view(game)
    arcade.run()
if __name__ == "__main__":
    main()