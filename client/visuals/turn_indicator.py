import pyglet


class TurnIndicator:
    class __TurnIndicator(pyglet.sprite.Sprite):
        red_image = pyglet.resource.image('assets/turn-red.png')
        blue_image = pyglet.resource.image('assets/turn-blue.png')

        def __init__(self, nxt):
            super().__init__(img=self.red_image, x=0, y=0)
            self.change_image(nxt)

        def change_image(self, nxt):
            if nxt == -1:
                self.image = self.blue_image
            else:
                self.image = self.red_image

    instance = None

    def __init__(self, nxt):
        if not TurnIndicator.instance:
            TurnIndicator.instance = TurnIndicator.__TurnIndicator(nxt)

    def __getattr__(self, item):
        return getattr(self.instance, item)
