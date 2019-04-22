import unittest
import numpy as np
from tests import fixtures as fix
import game_logic as logic


class TestLogic(unittest.TestCase):

    state = np.zeros((10, 10))

    def setUp(self):
        pass

    def test_turn(self):
        """
        Test if function turn alternates users
        """
        self.assertEqual(logic.turn('red'), 'blue')
        self.assertEqual(logic.turn('blue'), 'red')

    def test_check_game_state_dim(self):
        np.testing.assert_array_equal(logic.check_game_state(fix.state_2_3, 3),
                                      np.array([[2,1], [2, 2], [2, 3]]))


if __name__ == '__main__':
    unittest.main()
