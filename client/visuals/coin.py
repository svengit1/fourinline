import pyglet


class Coin(pyglet.sprite.Sprite):

    red_image = pyglet.resource.image('assets/coin-red.png')
    blue_image = pyglet.resource.image('assets/coin-blue.png')

    def __init__(self, x, y, batch, player, group, board_position):
        super().__init__(img=self.red_image, x=x, y=y, batch=batch)
        self.scale = 0.35
        self.group = group
        self.board_position = board_position
        self.image = Coin.player_image(player)

    def get_position(self):
        return self.board_position

    @staticmethod
    def player_image(player):
        if player == -1:
            return Coin.blue_image
        return Coin.red_image


