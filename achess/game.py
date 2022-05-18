import chess
import output

class ChessGame():
	def __init__(self, *args, **kwargs):
		self.colors = ['Black', 'White']

	def createBoard(self):
		newBoard = chess.Board()
		newBoard.focus = 0
		return newBoard

	def checkLocation(self, loc):
		if loc not in chess.SQUARES:
			raise ValueError(f"Error: {loc} not in chessboard.")

	def getSquareData(self, board, loc):
		self.checkLocation(loc)

		squareData = {}
		squareData["name"] = chess.square_name(loc)
		if board.piece_at(loc) == True:
			squareData["piece"] = chess.piece_name(board.piece_type_at(loc))
		if board.color_at(loc) == True:
			squareData["color"] = board.color_at(loc)
		return squareData

	def listSquares(self, board, squareList):
		if not type(squareList) == chess.SquareSet:
			raise ValueError("Error: Not a square set.")
		squares = {}
		for square in squareList:
			if type(square) == int:
				squares[square] = self.getSquareData(board, square)
		return squares

	def setFocus(self, board, loc):
		self.checkLocation(loc)
		board.focus = loc
		return loc

	def validateMove(self, board, start, end, promotion=None):
		self.checkLocation(start)
		self.checkLocation(end)
		turn = board.getTurn()
		startSquare = self.getSquareData(board, start)
		endSquare = self.getSquareData(board, end)
		move = chess.Move(start, end, promotion)
		if move not in board.legal_moves:
			raise ValueError("Illegal move.")
		else:
			return move, startSquare, endSquare, promotion

