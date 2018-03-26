import unittest
from creature import Hero, Monster
import room


class TestFighting(unittest.TestCase):

    def test_fight(self):
        weak = Monster("Blob", 2, None, None)
        strong = Hero("Lucas", 400, None, None)
        self.assertEqual(room.fight(weak,strong), strong)


if __name__ == '__main__':
    unittest.main()