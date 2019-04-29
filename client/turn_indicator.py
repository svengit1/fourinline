import pyglet


class TurnIndicator:
    class __TurnIndicator(pyglet.sprite.Sprite):
        red_image = pyglet.resource.image('assets/turn-red.png')
        blue_image = pyglet.resource.image('assets/turn-blue.png')

        def __init__(self):
            pyglet.sprite.Sprite.__init__(self, img=self.blue_image, x=0, y=0)

        def switch_image(self):
            if self.image == self.red_image:
                self.image = self.blue_image
            else:
                self.image = self.red_image

    instance = None

    def __init__(self):
        if not TurnIndicator.instance:
            TurnIndicator.instance = TurnIndicator.__TurnIndicator()

    def __getattr__(self, item):
        return getattr(self.instance, item)
