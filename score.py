import pyglet
class Score:
    score = 0

    def message(self):
        return 'Score: {0}'.format(str(self.score))

    def label(self):
        return pyglet.text.Label(self.message(),
                     font_name='Times New Roman',
                     font_size=36,
                     x=10,
                     y=10)

    def add(self, amount):
        self.score = self.score + amount

    def reset(self):
        self.score = 0