from pyglet import sprite as s
from pyglet import image as i
from pyglet.window import key
from pyglet import shapes
import math

class Rocket:

    def __init__(self, width, height, xStart, yStart, velocity):
        self.width = width
        self.height = height
        self.xStart = xStart
        self.yStart = yStart
        self.velocity = velocity
        self.sprite = self.create()
        self.radarLength = 300
        self.radars = self.createRadars()
        self.rotationWeight = 15
        self.direction = key.UP
        self.steering = False
        self.alive = True
        self.radarData = [0, 0, 0, 0, 0]

    def create(self):
        image = i.load('resources/rocket.png')
        image.anchor_x = image.width//2
        image.anchor_y = image.height//2
        sprite = s.Sprite(image, x= self.xStart, y=self.yStart)
        sprite.scale = self.height/400
        return sprite

    def createRadars(self):
        radars = []
        for radar in range(5):
            radars.append(shapes.Line(self.sprite.x, self.sprite.y, self.sprite.x, self.sprite.y))

        return radars

    def drawRadars(self):
        for radar in self.radars:
            radar.draw()

    def updateRadar(self):
        rotations = [270, 315, 0, 45, 90]
        for i, radar in enumerate(self.radars):
            radar.x = self.sprite.x
            radar.y = self.sprite.y

            radians = math.radians(rotations[i] + self.sprite.rotation)
            radar.x2= self.sprite.x + (math.cos(radians) * self.radarLength)
            radar.y2 = self.sprite.y + (math.sin(radians) * -self.radarLength)

    def left(self):
        # if self.sprite.rotation < 0:
        #     self.sprite.rotation = 360
        # self.sprite.rotation = self.sprite.rotation - self.rotationWeight
        self.sprite.y += self.velocity

    def right(self):
        # if self.sprite.rotation > 360:
        #     self.sprite.rotation = 0
        # self.sprite.rotation = self.sprite.rotation + self.rotationWeight
        self.sprite.y -= self.velocity

    def translate(self):
        self.updateRadar()
        # radians = math.radians(self.sprite.rotation)
        # self.sprite.position = (self.sprite.x + (math.cos(radians) * self.velocity),
        #                         self.sprite.y + (math.sin(radians) * -self.velocity))
        # pass

    def respawn(self):
        self.sprite.x = self.xStart
        self.sprite.y = self.yStart
        self.sprite.rotation = 0
        self.radarData = [0, 0, 0, 0, 0]
        self.alive = True
