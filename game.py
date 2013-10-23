class Game(object):
	BLANK = 2

	def __init__(self, first_player=0):
		self.current_player = first_player
		self.board = [self.BLANK] * 9

	@property
	def next_player(self):
		return (self.current_player + 1) % 2

	def play(self, pos):
		pos -= 1
		self.board[pos] = self.current_player
		self.current_player = self.next_player

	def winner(self, player):
		return any([all([x == player for x in row]) for row in self.rows]) or \
			   any([all([x == player for x in col]) for col in self.cols]) or \
			   any([all([x == player for x in diag]) for diag in self.diags])

	@property
	def cols(self):
		b = self.board
		return [[b[x], b[x+3], b[x+6]] for x in range(3)]

	@property
	def rows(self):
		b = self.board
		return [[b[x], b[x+1], b[x+2]] for x in [0, 3, 6]]

	@property
	def diags(self):
		b = self.board
		return [[b[0], b[4], b[8]], 
				[b[2], b[4], b[6]]]

	def valid_moves(self):
		return [i for i, x in enumerate(self.board) if x == self.BLANK]

