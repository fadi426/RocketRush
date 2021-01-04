import random

from pyglet import shapes

import asteroid as a

import rocket as r
class Map:

    def __init__(self, window):
        self.rockets = []
        self.window = window
        self.asteroids = []

    def createRockets(self, amount):
        for i in range(amount):
            rocket = r.Rocket(self.window.width / 30,
                              self.window.height / 10,
                              self.window.width / 10,
                              self.window.height / 2,
                              15)
            self.rockets.append(rocket)

    def createAsteroids(self, amount):
        for i in range(amount):
            position = self.calculateRandomPosition()
            x = position[0]
            y = position[1]
            asteroid = a.Asteroid(x, y, self.window.width / 10, self.window.height / 10, 5, 10)
            self.asteroids.append(asteroid)

    def updateRadars(self, r):
        for i, radar in enumerate(r.radars):
            for a in self.asteroids:
                r.radarData[i] = ((radar.x2 - a.sprite.x) ** 2 + (radar.y2 - a.sprite.y) ** 2)
        # print(r.radarData)

    def draw(self):
        self.drawRockets()
        self.drawAsteroids()

    def drawRockets(self):
        for rocket in self.rockets:
            if rocket.alive == True:
                rocket.sprite.draw()
                # rocket.drawRadars()
                rocket.translate()
                self.updateRadars(rocket)
                self.collision(rocket)
                self.outOfBounds(rocket)


    def drawAsteroids(self):
        for asteroid in self.asteroids:
            if asteroid.sprite.x < -asteroid.width \
                    or asteroid.sprite.y < -asteroid.height * 2 \
                    or asteroid.sprite.y > self.window.height + asteroid.height * 2:
                position = self.calculateRandomPosition()
                x = position[0]
                y = position[1]
                asteroid.spawn(x, y)
            asteroid.sprite.draw()
            asteroid.translate()

    def collision(self, r):
        for a in self.asteroids:
            distance = (r.sprite.x - a.sprite.x) ** 2 + (r.sprite.y - a.sprite.y) ** 2
            if distance < (r.sprite.width / 2 + a.sprite.width / 2) ** 2:
                r.alive = False

    def outOfBounds(self, r):
        if r.sprite.x > self.window.width:
            r.sprite.x = 0
        if r.sprite.x < 0:
            r.sprite.x = self.window.width

        if r.sprite.y > self.window.height:
            r.sprite.y = 0
        if r.sprite.y < 0:
            r.sprite.y = self.window.height

        # if r.sprite.x >= self.window.width \
        #         or r.sprite.x <= 0 \
        #         or r.sprite.y >= self.window.height \
        #         or r.sprite.y <= 0:
        #     r.alive = False

    def gameOver(self):
        for r in self.rockets:
            if r.alive:
                return False
        return True

    def calculateRandomPosition(self):
        xOffset = 1000
        x = random.randrange(self.window.width + xOffset/2, self.window.width + xOffset)
        y = random.randrange(0, self.window.height)
        return x,y