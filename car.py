import pyglet, math
from pyglet.gl import *
from Vector import Vector2D
from typing import NewType

key = pyglet.window.key
speed = 3.0

class Car():
    def __init__(self, x: int, y: int):
        self.x_coord = x
        self.y_coord = y
        self.v_acceleration = Vector2D(0,0)
        self.v_velocity = 0
        self.rotation = 0

    def drawCar(self):
        self.car = pyglet.sprite.Sprite(pyglet.resource.image('../Images/car.png'), x=self.x_coord, y=self.y_coord)
        self.car.scale = 0.2
        self.car.anchor_x = self.car.width // 2
        self.car.anchor_y = self.car.height // 2
        self.car.rotation = self.rotation
        self.car.draw()

    # def drawInfo(self):
    #     self.labelA = pyglet.text.Label(self.v_acceleration, font_name='Times New Roman', font_size=36, x=400, y=300, anchor_x='center', anchor_y='center')
    #     self.labelV = pyglet.text.Label(self.v_velocity, font_name='Times New Roman', font_size=36, x=400, y=300, anchor_x='center', anchor_y='center')

    def forward(self):
        self.v_acceleration += Vector2D(1,0)

    def backward(self):
        self.v_acceleration -= Vector2D(1,0)

    def update(self):
        self.v_velocity = self.v_acceleration * speed
        self.rotation = self.v_velocity.rotation()


class main(pyglet.window.Window):
    def __init__ (self, width=800, height=600, fps=False, *args, **kwargs):
        super(main, self).__init__(width, height, *args, **kwargs)
        self.x, self.y = 0, 0
        self.alive = 1

        self.CAR = Car(400, 300)
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

    def on_draw(self):
        self.render()

    def on_close(self):
        self.alive = 0

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.alive = 0

        if symbol == key.UP:
            self.up_pressed = True

        if symbol == key.DOWN:
            self.down_pressed = True

        if symbol == key.LEFT:
            self.left_pressed = True

        if symbol == key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.up_pressed = False

        if symbol == key.DOWN:
            self.down_pressed = False

        if symbol == key.LEFT:
            self.left_pressed = False

        if symbol == key.RIGHT:
            self.right_pressed = False

    def render(self):
        self.clear()

        self.CAR.drawCar()
        # self.CAR.drawInfo()
        
        if self.up_pressed == True:
            self.CAR.forward()
            print(self.CAR.v_acceleration)
            self.CAR.update()
            print(self.CAR.v_velocity)
            print(self.CAR.rotation)
        if self.down_pressed == True:
            self.CAR.backward()
            print(self.CAR.v_acceleration)
            self.CAR.update()
            print(self.CAR.v_velocity)
            print(self.CAR.rotation)
        # if self.left_pressed == True:
        #     self.CAR.rotation -= 1
        # if self.right_pressed == True:
        #     self.CAR.rotation += 1
            
        self.flip()

    def run(self):
        while self.alive == 1:
            self.render()

            event = self.dispatch_events()

if __name__ == '__main__':
    x = main()
    x.run()
