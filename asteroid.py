import math

from pyglet import image as i
from pyglet import sprite as s
import random

class Asteroid:

    def __init__(self, x, y, width, height, rotationSpeed, velocity):
        self.width = width
        self.height = height
        self.rotationSpeed = rotationSpeed
        self.velocity = velocity
        self.sprite = self.create(x, y)
        self.translationMode = self.setTranslation()

    def create(self, x, y):
        image = i.load('resources/asteroid.png')
        image.anchor_x = image.width//2
        image.anchor_y = image.height//2
        sprite = s.Sprite(image, x=x, y=y)
        sprite.scale = self.height/random.randrange(60,70)
        return sprite

    def rotate(self):
        if self.sprite.rotation > 360:
            self.sprite.rotation = 0
        self.sprite.rotation += 0.3

    def translate(self):
        if self.translationMode == 1:
            angle = 185
        elif self.translationMode == 2:
            angle = 105
        else:
            angle = 180

        radians = math.radians(angle)
        self.sprite.position = (self.sprite.x + (math.cos(radians) * self.velocity),
                                self.sprite.y + (math.sin(radians) * -self.velocity))

        self.rotate()

    def setTranslation(self):
        self.translationMode = random.randrange(1, 4)

    def spawn(self, x, y):
        self.setTranslation()
        self.sprite.rotation = 0
        self.sprite.x = x
        self.sprite.y = y