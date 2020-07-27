import unittest
from soccer_assignment import SoccerLeague


class SoccerLeagueTest(unittest.TestCase):

    def setUp(self):
        self.original_list = [['Lions 3', 'Snakes 3'], ['Tarantulas 1', 'FC Awesome 0'],
                              ['Lions 1', 'FC Awesome 1'], ['Tarantulas 3', 'Snakes 1'],
                              ['Lions 4', 'Grouches 0']]
        self.soccer_league_class = SoccerLeague()
        self.split = self.soccer_league_class.split_data(self.original_list)
        self.compare = self.soccer_league_class.compare_scores(self.original_list)
        self.sort = self.soccer_league_class.sort_results(self.original_list)
        self.rank = self.soccer_league_class.rank_teams(self.original_list)

    def test_list_equal_split(self):
        self.assertNotEqual(self.original_list, self.split)

    def test_list_equal_compare(self):
        self.assertNotEqual(self.original_list, self.compare)

    def test_list_equal_sort(self):
        self.assertNotEqual(self.original_list, self.sort)

    def test_list_equal_rank(self):
        self.assertNotEqual(self.original_list, self.rank)

    def test_split_func(self):
        split_data = [[['Lions', '3'], ['Snakes', '3']],
                      [['Tarantulas', '1'], ['FC Awesome', '0']],
                      [['Lions', '1'], ['FC Awesome', '1']],
                      [['Tarantulas', '3'], ['Snakes', '1']],
                      [['Lions', '4'], ['Grouches', '0']]]
        self.assertTrue(self.split, split_data)
        self.assertEqual(self.split, split_data)

    def test_compare_func(self):
        compare_data = ({'Lions': 5, 'Snakes': 1,
                         'Tarantulas': 6, 'FC Awesome': 1,
                         'Grouches': 0})
        self.assertTrue(self.compare, compare_data)
        self.assertEqual(self.compare, compare_data)

    def test_sort_func(self):
        sort_data = [('Tarantulas', 6), ('Lions', 5),
                     ('FC Awesome', 1), ('Snakes', 1),
                     ('Grouches', 0)]
        self.assertTrue(self.sort, sort_data)
        self.assertEqual(self.sort, sort_data)

    def test_rank_func(self):
        rank_data = "1. Tarantulas 6 pts\n2. Lions 5 pts\n3. FC Awesome 1 pt\n3. Snakes 1 pt\n5. Grouches 0 pts\n"
        self.assertTrue(self.rank, rank_data)
        self.assertEqual(self.rank, rank_data)


if __name__ == '__main__':
    unittest.main()