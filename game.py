import random
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


	def players(self):
    	starter = raw_input("Do you require the first move? (y/n): ")
    	if starter == "y":
        	print "\nThen take the first move. You will need it."
        	human = 0
        	computer = 1
        	human = current_player()
  		else:
        	print "\nComputer goes first"
        	computer = 0
        	human = 1
        	computer = self.current_player()
    	return computer, human



	def computer_play(self):
		pos = random.choice(self.valid_moves())
		return pos

	def human_play(self):
		valid = self.valid_moves()
		pos = None
		print "It is your turn"
		while pos not in valid:
			pos =  int(raw_input("Your move:))
			if pos not in valid:
				print "still an invalid move"
			return pos	


	@property
	def draw_board(self):
		b = self.board

		for i in b:
			if i == 0:
				b[i] = "X"
			if i == 1:
				b[i] = "O"
			else:
				pass

		print "|",b[0],"|",b[1],"|",b[2],"|"
		print "|",b[3],"|",b[4],"|",b[5],"|"
		print "|",b[6],"|",b[7],"|",b[8],"|"

while True:
	g = Game(object)

	print "Welcome to a game of tic tac toe"	
	print "Here's your board"
	
	g.draw_board

	g.players()

	human = g.players()
	computer = g.players()

	turn = 0

	while not winner(g.players()):
		if turn == human:
			pos = g.human_play()
			g.play(pos)
		else:
			pos =  g.computer_play()
			g.play(pos)
		turn =  next_player()
	break



	


	

