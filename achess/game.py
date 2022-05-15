import chess
import output

class ChessGame():
	def __init__(self, *args, **kwargs):
		self.colors = ['Black', 'White']

	def createBoard(self):
		newBoard = chess.Board()
		newBoard.focus = 0

	def checkLocation(self, loc):
		if loc not in chess.SQUARES:
			raise ValueError(f"Error: {loc} not in chessboard.")

	def getSquareData(self, board, loc):
		self.checkLocation(loc)

		squareData = {}
		squareData["name"] = chess.square_name(loc)
		squareData["piece"] = chess.piece_name(board.piece_type_at(loc))
		if squareData["piece"]:
			squareData["color"] = self.colors[board.color_at(loc)]
		return squareData

	def getTurn(self, board):
		return self.colors[board.turn]

	def setFocus(self, board, loc):
		self.checkLocation(loc)
		board.focus = loc
		return loc

	def move(self, board, start, end, promotion=None):
		capturestring = ""
		self.checkLocation(start)
		self.checkLocation(end)
		turn = board.getTurn()
		startSquare = self.getSquareData(board, start)
		endSquare = self.getSquareData(board, end)
		move = chess.Move(start, end, promotion)
		if move not in board.legal_moves:
			output.say("Illegal move!")
		else:
			board.push(move)
		movestring = "Moved {} {} from {} to {}".format(startSquare["color"], startSquare["piece"], startSquare["name"], endSquare["name"])
		if endSquare["piece"]:
			capturestring = "Captured {}".format(endSquare["piece"])
		output.say("{}. {}".format(movestring, capturestring))