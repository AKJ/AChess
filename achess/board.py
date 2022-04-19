import chess
import output
import wx

from keyboard_handler.wx_handler import WXControlKeyboardHandler

class ChessBoard(wx.Panel):

	def __init__(self, parent, id, game, loc, *args, **kwargs):
		super(ChessBoard, self).__init__(parent, id, *args, **kwargs)
		self.board = game
		self.colors = ['Black', 'White']
		self.handler = WXControlKeyboardHandler(parent)
		self.location = loc
		self.marked = ""
		self.register_keys()

	def checkLocation(self):
		if self.location not in chess.SQUARES:
			raise ValueError("Error: {} not in chessboard.".format(self.location))

	def readSquare(self, loc):
		self.checkLocation()	

		square = chess.square_name(loc)
		piece = self.board.piece_at(loc)
		if piece:
			pieceColor = self.colors[piece.color]
			pieceName = chess.piece_name(piece.piece_type)
			answer = f"{square}, {pieceColor} {pieceName}"
		else:
			answer = f"{square}"
		output.say(answer)

	# Handlers for keyboard keys
	def register_keys(self):
		self.handler.register_key("up", self.handle_up)
		self.handler.register_key("down", self.handle_down)
		self.handler.register_key("left", self.handle_left)
		self.handler.register_key("right", self.handle_right)
		self.handler.register_key("space", self.handle_space)
		
	def handle_up(self):
		self.checkLocation()
		if self.location not in range(56, 63):
			self.location = self.location+8
		self.readSquare(self.location)

	def handle_down(self):
		self.checkLocation()
		if self.location not in range(0, 7):
			self.location = self.location - 8
		self.readSquare(self.location)

	def handle_left(self):
		self.checkLocation()
		if self.location not in range(0, 56, 8):
			self.location = self.location - 1
		self.readSquare(self.location)

	def handle_right(self):
		self.checkLocation()
		if self.location not in range(7, 63, 8):
			self.location = self.location + 1
		self.readSquare(self.location)

	def handle_space(self):
		piece = self.board.piece_at(self.location)
		def mark():
			self.marked = self.location
			output.say(f"{self.colors[piece.color]} {chess.piece_name(piece.piece_type)} selected.")
		if self.marked not in chess.SQUARES:
			if not self.board.color_at(self.location) == self.board.turn:
				output.say("Invalid piece.")
			else:
				mark()
		elif self.marked == self.location:
			self.marked = ''
			output.say(f"{chess.piece_name(piece.piece_type)} unselected.")
		else:
			self.move(self.marked, self.location)

	def move(self, start, end):
		enemy = self.board.piece_at(end)
		move = chess.Move(start, end)
		if move not in self.board.legal_moves:
			output.say("Illegal move!")
		else:
			self.board.push(move)
			self.marked = ''
			answer = f"Moved {chess.piece_name(self.board.piece_at(end).piece_type)} from {chess.square_name(start)} to {chess.square_name(end)}"
			output.say(answer)
