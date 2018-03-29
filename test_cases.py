import unittest
from creature import Hero, Monster
import room


class TestFighting(unittest.TestCase):

    def test_fight(self):
        weak = Monster()
        weak.health = 1
        strong = Hero("Lucas")
        strong.weapons[0].max_damage = 10
        self.assertEqual(room.fight(weak, strong), strong)


if __name__ == '__main__':
    unittest.main()
