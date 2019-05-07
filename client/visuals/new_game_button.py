import pyglet


class NewGameButton:
    class __NewGameButton(pyglet.sprite.Sprite):
        new_game_button = pyglet.resource.image('assets/new-game.png')

        def __init__(self):
            super().__init__(img=self.new_game_button, x=290, y=0)

        def is_clicked(self, x, y):
            if self.x < x < self.x + self.width and self.y < y < self.y + self.width:
                return True
            return False

    instance = None

    def __init__(self):
        if not NewGameButton.instance:
            NewGameButton.instance = NewGameButton.__NewGameButton()

    def __getattr__(self, item):
        return getattr(NewGameButton.instance, item)
