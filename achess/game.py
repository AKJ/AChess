import chess
import output

class ChessGame():
	def __init__(self, board, colors, focus, *args, **kwargs):
		self.board = chess.Board()
		self.colors = ['Black', 'White']
		self.focus = 0 # For now

	def checkLocation(self, loc):
		if loc not in chess.SQUARES:
			raise ValueError(f"Error: {loc} not in chessboard.")

	def getSquareData(self, loc):
		self.checkLocation(loc)

		squareData = {}
		squareData["name"] = chess.square_name(loc)
		squareData["piece"] = self.board.piece_type_at(loc)
		squareData["color"] = self.colors[self.board.color_at(loc)]
		return squareData

	def getTurn(self):
		return self.colors[self.board.turn]

	def setFocus(self, loc):
		self.checkLocation(loc)
		self.focus = loc
		return loc

	def move(self, start, end):
		self.checkLocation(start)
		self.checkLocation(end)
		startSquare = self.getSquareData(start)
		endSquare = self.getSquareData(end)
		move = chess.Move(start, end)
		if move not in self.board.legal_moves:
			output.say("Illegal move!")
		else:
			self.board.push(move)
		movestring = "Moved {} {} from {} to {}".format(startSquare["color"], startSquare["piece"], startSquare["name"], endSquare["name"])
		capturestring = "Captured {}.".format(endSquare["piece"])
		output.say(f"{movestring}. {capturestring}.")