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

    def test_check_detect_same_in_rows(self):
        np.testing.assert_array_equal(logic.check_game_state(fix.state_1, 3, 1),
                                      fix.result_1)

    def test_check_detect_same_in_columns(self):
        np.testing.assert_array_equal(logic.check_game_state(fix.state_2, 3, 1),
                                      fix.result_2)



if __name__ == '__main__':
    unittest.main()
