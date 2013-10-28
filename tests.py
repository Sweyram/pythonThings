import unittest
import game

class GameTest(unittest.TestCase):
	def test_game_start(self):
		g = game.Game()
		self.assertTrue(all([x == 2 for x in g.board]))

	def test_first_player(self):
		g = game.Game()
		self.assertEqual(0, g.current_player)

	def test_next_player(self):
		g = game.Game(1)
		self.assertEqual(1, g.current_player)
		self.assertEqual(0, g.next_player)

	def test_play(self):
		g = game.Game(1)

		self.assertEqual(range(9), g.valid_moves())

		g.play(1)
		self.assertEqual(0, g.current_player)

		g.play(2)
		self.assertEqual([1, 0] + ([g.BLANK] * 7),
						 g.board)

		self.assertEqual(range(2, 9),
						 g.valid_moves())

	def test_cols(self):
		g = game.Game(1)
		g.play(1)
		g.play(2)
		self.assertEqual([[1, 2, 2], [0, 2, 2], [2, 2, 2]],
						 g.cols)

	def test_rows(self):
		g = game.Game(1)
		g.play(1)
		g.play(2)
		self.assertEqual([[1, 0, g.BLANK], [g.BLANK] * 3, [g.BLANK] * 3],
						 g.rows)

	def test_game_won(self):
		g = game.Game(0)
		for i in [5, 3, 1, 9, 4, 6]:
			g.play(i)
		self.assertEqual([0, 2, 1, 0, 0, 1, 2, 2, 1],
						 g.board)

		self.assertFalse(g.winner(0))
		self.assertTrue(g.winner(1))

	def test_draw_board(self):
		g = game.Game()
		for i in [5,3,1,9,4,6]:
			g.play(i) 
		self.assertEqual("|X|2|O|\n|X|X|O|\n|2|2|O|" , g.draw_board)
		

if __name__ == '__main__':
	unittest.main()